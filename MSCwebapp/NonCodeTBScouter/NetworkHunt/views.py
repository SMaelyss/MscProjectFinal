from django.shortcuts import render
from multiprocessing import context
from django.db import connection

from django.db.models import Q
from django.views import View

from .forms import NH_nameid_form
from .models import Modules, ModuleCorrelation, Elements, Relations, Samples, GrowthConditions, GoTerms, Srna, Utr, AnnotatedNcrna, Cds


import plotly.express as px
import plotly as pt
import pandas as pd

# Create your views here.
def NetworkHunt_homepage(request):
  
  srna_ids = list(Srna.objects.values_list('srna_element_id', flat=True))
  srna_names = list(Srna.objects.values_list('srna_name', flat=True))
  suggestions_srna = srna_ids + srna_names
  
  utr_ids = list(Utr.objects.values_list('utr_element_id', flat=True))
  utr_names = list(Utr.objects.values_list('predicted_utr_name', flat=True))
  suggestions_utr = utr_ids + utr_names

  annotatedncrna_ids = list(AnnotatedNcrna.objects.values_list('annotated_ncrna_element_id', flat=True))
  annotatedncrna_name = list(AnnotatedNcrna.objects.values_list('annotated_ncrna_name', flat=True))
  suggestions_annotatedncrna = annotatedncrna_ids + annotatedncrna_name

  cds_ids = list(Cds.objects.values_list('cds_element_id', flat=True))
  cds_names = list(Cds.objects.values_list('cds_name', flat=True))
  suggestions_cds = cds_ids + cds_names

  #suggestions_zip = zip(suggestions_annotatedncrna, suggestions_cds, suggestions_srna, suggestions_utr)
  #print(ni_form)

  ni_form= NH_nameid_form()

  context = {
    'ni_form' : ni_form,
    #'suggestions_zip': suggestions_zip,
    'suggestions_annotatedncrna' : suggestions_annotatedncrna,
    'suggestions_cds' : suggestions_cds,
    'suggestions_utr' : suggestions_utr,
    'suggestions_srna' : suggestions_srna,

  }

  return render(request, 'NetworkHunt.html', context)


def NetworkHunt_results(request):
  ni_form = NH_nameid_form(request.POST)

# Method:POST           
  if request.method == 'POST' :
    print('Method is POST')
    ni_form = NH_nameid_form(request.POST)
    form_request = (request.POST)

# Form validity
    if ni_form.is_valid() :
      print('form is valid')

# (Location) or (Name and ID)
# >Name and ID search
      if 'dd_ni_submit' in form_request:
          request_denomer = 'ni_request'

# Clean front end input
          ni_data_nameid = str(ni_form.cleaned_data['ui_element'])
          ni_data_type = str(ni_form.cleaned_data['ui_type'])
          ni_data_text_raw = [ni_form.cleaned_data['ui_text_srna']] + [ni_form.cleaned_data['ui_text_utr']] + [ni_form.cleaned_data['ui_text_cds']] + [ni_form.cleaned_data['ui_text_ancrna']]
          ni_data_text = ''.join(list(filter(None, ni_data_text_raw)))
          ni_mm = str(ni_form.cleaned_data['ui_mm'])
          ni_raw_cor = str(ni_form.cleaned_data['ui_raw_cor'])
   
          #print(type(ni_raw_cor))


# Get element id
          def return_element_id(ni_data_type, ni_data_text, ni_data_nameid):
            if ni_data_nameid == 'id':
              if ni_data_type == 'Srna':
                element_id = Srna.objects.filter(srna_element_id=ni_data_text).values_list('srna_element_id', flat=True)
              elif ni_data_type == 'Utr':
                element_id = list(Utr.objects.filter(utr_element_id=ni_data_text).values_list('utr_element_id', flat=True))
              elif ni_data_type == 'Cds':
                element_id = list(Cds.objects.filter(cds_element_id=ni_data_text).values_list('cds_element_id', flat=True))
              elif ni_data_type == 'Annotated_ncrna':
                element_id = list(AnnotatedNcrna.objects.filter(annotated_ncrna_element_id=ni_data_text).values_list('annotated_ncrna_element_id', flat=True))

            else:
              if ni_data_type == 'Srna':
                element_id = list(Srna.objects.filter(srna_name=ni_data_text).values_list('srna_element_id', flat=True))
              
              elif ni_data_type == 'Utr':
                element_id = list(Utr.objects.filter(predicted_utr_name=ni_data_text).values_list('utr_element_id', flat=True))
              elif ni_data_type == 'Cds':
                element_id = list(Cds.objects.filter(cds_name=ni_data_text).values_list('cds_element_id', flat=True))
              elif ni_data_type == 'Annotated_ncrna':
                element_id = list(AnnotatedNcrna.objects.filter(annotated_ncrna_name=ni_data_text).values_list('annotated_ncrna_element_id', flat=True))

            if not element_id:
              element_id = list('e')
            #print(element_id)
            print(connection.queries)
            return element_id
          element_id = list(return_element_id(ni_data_type, ni_data_text, ni_data_nameid))[0]

# Check for element None type
          if element_id != 'e':

            def visual_network_graph(element_id, ni_data_type, ni_mm):
              module_id = Relations.objects.filter(element_id=element_id).values_list('module_id',flat=True)[0]
              network_element_ids =  Relations.objects.filter(Q(module_id=module_id) & Q(module_match_score__gt=ni_mm)).values_list('element_id',flat=True)
              network_element_types = Relations.objects.filter(Q(module_id=module_id) & Q(module_match_score__gt=ni_mm)).values_list('element_type',flat=True)
              network_element_mm = Relations.objects.filter(Q(module_id=module_id) & Q(module_match_score__gt=ni_mm)).values_list('module_match_score',flat=True)

              
              network_elements_data = zip(network_element_ids, network_element_types,network_element_mm )
              
              target_attribute = list(network_element_types)
              target_nodes = list(network_element_ids)

              count = 0

              source_attribute = list()
              source_nodes = list()

              while count <  len(target_nodes):
                count += 1
                source_nodes.append(element_id)
                source_attribute.append(ni_data_type)

              # get the related genes elements 
              if ni_data_type == 'Srna':
                sn1 = Srna.objects.filter(srna_element_id=element_id).values_list('gene_element_id', flat=True)[0]
                source_nodes.append(element_id)
                source_attribute.append(ni_data_type)
                target_nodes.append(sn1)
                target_attribute.append('Cds')

              elif ni_data_type == 'Utr':
                sn1 = Utr.objects.filter(utr_element_id=element_id).values_list('downstream_gene_element_id', flat=True)[0]
                sn12 = Utr.objects.filter(utr_element_id=element_id).values_list('upstream_gene_element_id', flat=True)[0]

                source_nodes.append(element_id)
                source_attribute.append(ni_data_type)
                target_nodes.append(sn1)
                target_attribute.append('Cds')

                source_nodes.append(element_id)
                source_attribute.append(ni_data_type)
                target_nodes.append(sn12)
                target_attribute.append('Cds')
            
              elif ni_data_type == 'Annotated_ncrna':
                sn1 = AnnotatedNcrna.objects.filter(annotated_ncrna_element_id=element_id).values_list('related_srna_name', flat=True)[0]
                source_nodes.append(element_id)
                source_attribute.append(ni_data_type)
                target_nodes.append(sn1)
                target_attribute.append('Srna')
            
              types = ''
            
          
          
          
              sn2 = list(network_element_ids)
              for id in sn2:
                types = Relations.objects.filter(element_id=id).values_list('element_type',flat=True)[0]
              if types == 'utr':
                sn3 = Utr.objects.filter(utr_element_id=id).values_list('downstream_gene_element_id', flat=True)[0]
                sn4 = Utr.objects.filter(utr_element_id=id).values_list('upstream_gene_element_id', flat=True)[0]
                source_nodes.append(id)
                source_attribute.append(types)
                target_nodes.append(sn3)
                target_attribute.append('cds')
                source_nodes.append(id)
                source_attribute.append(types)
                target_nodes.append(sn4)
                target_attribute.append('cds')
            
              if types == 'srna':
                sn3 = Srna.objects.filter(srna_element_id=id).values_list('gene_element_id', flat=True)[0]
                source_nodes.append(id)
                source_attribute.append(types)
                target_nodes.append(sn3)
                target_attribute.append('cds')
              if types == 'Annotated_ncrna':
                sn3 = AnnotatedNcrna.objects.filter(annotated_ncrna_element_id=id).values_list('related_srna_name', flat=True)[0]
                source_nodes.append(id)
                source_attribute.append(types)
                target_nodes.append(sn3)
                target_attribute.append('srna')

                id_count = 0
            
              return_edge_zip = zip(source_nodes, target_nodes) 
  
              return source_nodes, source_attribute, target_nodes, target_attribute , return_edge_zip, network_elements_data 

            s_nodes =visual_network_graph(element_id, ni_data_type,ni_mm )[0]
            t_nodes =visual_network_graph(element_id, ni_data_type, ni_mm)[2]
            s_attribute =visual_network_graph(element_id, ni_data_type,ni_mm)[1]
            t_attribute =visual_network_graph(element_id, ni_data_type,ni_mm)[3]
            edge_zip =visual_network_graph(element_id, ni_data_type,ni_mm)[4]

            ned = visual_network_graph(element_id, ni_data_type,ni_mm)[5]
           

        

            all_nodes = s_nodes + t_nodes

            all_attributes = s_attribute + t_attribute
            all_attributes = ['#7BE141' if item == 'utr' else item for item in all_attributes]
            all_attributes = ['#7BE141' if item == 'Utr' else item for item in all_attributes]
            all_attributes = ['#c6637b' if item == 'Srna' else item for item in all_attributes]
            all_attributes = ['#c6637b' if item == 'srna' else item for item in all_attributes]
            all_attributes = ['#8de8e8' if item == 'cds' else item for item in all_attributes]
            all_attributes = ['#8de8e8' if item == 'Cds' else item for item in all_attributes]
            all_attributes = ['#f9e099' if item == 'annotated_ncrna' else item for item in all_attributes]
            all_attributes = ['#f9e099' if item == 'Annotated_ncrna' else item for item in all_attributes]

            nodes_zip = zip(all_nodes, all_attributes)
            
            
            print(all_nodes.pop())
          
            for all_nodes, all_attributes in nodes_zip:
              if all_nodes is not None and all_attributes is not None:
    
                print(type(all_nodes))
                print(type(all_attributes))
                nodes_zip = sorted(set(nodes_zip))
              else:
                nodes_zip = ''  
              
           
        
            all_nodes =  sorted(set(all_nodes))



            def return_module_network(element_id, ni_raw_cor):
              module_id = Relations.objects.filter(element_id=element_id).values_list('module_id',flat=True)[0]
              network_summed_condition_name = list()
              
            
            # Allow users to obtain all item swith correlation score .
              if ni_raw_cor == '1': #all associated   
                print('ALL ASSOCIATED')    
                network_summed_condition_name = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('summed_condition_name', flat=True)]
                network_raw_cor = [i for i in  ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('raw_cor', flat=True)]
                network_p_adj = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('p_adjusted_cor', flat=True) ]

                print(network_summed_condition_name)
                print(type(network_summed_condition_name))


                condition_zip = zip(network_summed_condition_name, network_raw_cor, network_p_adj)
               
                return condition_zip

              elif ni_raw_cor == '0': #weakly correlated
              
                network_summed_condition_name_a = [i for i in  ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__gte=0, raw_cor__lt=0.5 )).values_list('summed_condition_name', flat=True)]
                network_summed_condition_name_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=0, raw_cor__gte=-0.5)).values_list('summed_condition_name', flat=True) ]
              
                network_raw_cor_a = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__gte=0,raw_cor__lt=0.5 )).values_list('raw_cor', flat=True) ]
                network_raw_cor_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=0, raw_cor__gte=-0.5)).values_list('raw_cor', flat=True) ]
                          
                network_p_adj_a = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__gte=0,raw_cor__lt=0.5 )).values_list('p_adjusted_cor', flat=True) ]
                network_p_adj_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=0, raw_cor__gte=-0.5)).values_list('p_adjusted_cor', flat=True) ]
                

                network_summed_condition_name = network_summed_condition_name_a + network_summed_condition_name_b
                network_p_adj = network_p_adj_a + network_p_adj_b
                network_raw_cor = network_raw_cor_a + network_raw_cor_b

                

                condition_zip = zip(network_summed_condition_name, network_raw_cor, network_p_adj)
                return condition_zip

              elif ni_raw_cor == '0.5': #strongly correlated
                network_summed_condition_name_a = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q( raw_cor__gte=0.5 )).values_list('summed_condition_name', flat=True) ]
                network_summed_condition_name_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=-0.5)).values_list('summed_condition_name', flat=True) ]
              
                network_raw_cor_a = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__gte=0.5 )).values_list('raw_cor', flat=True) ]
                network_raw_cor_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=-0.5)).values_list('raw_cor', flat=True) ]
                          
                network_p_adj_a = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__gte=0.5 )).values_list('p_adjusted_cor', flat=True) ]
                network_p_adj_b = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id) & Q(raw_cor__lte=-0.5)).values_list('p_adjusted_cor', flat=True) ]
                print(network_summed_condition_name_a)

                network_summed_condition_name = list(network_summed_condition_name_a) + list(network_summed_condition_name_b)
                network_p_adj = network_p_adj_a + network_p_adj_b
                network_raw_cor = network_raw_cor_a + network_raw_cor_b 
                
                

                condition_zip = zip(network_summed_condition_name, network_raw_cor, network_p_adj)
               
              


            
                return condition_zip
            
            conditions_table = return_module_network(element_id, ni_raw_cor)

            def pd_cor_graphs(element_id):
              module_id = Relations.objects.filter(element_id=element_id).values_list('module_id',flat=True)[0]
              

              plot_summed_condition_name = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('summed_condition_name', flat=True)]
              plot_raw_cor = [i for i in  ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('raw_cor', flat=True)]
              plot_p_adj = [i for i in ModuleCorrelation.objects.filter(Q(module_id=module_id)).values_list('p_adjusted_cor', flat=True) ]

              for i in range(0, len(plot_p_adj)):
                plot_p_adj[i] = int(plot_p_adj[i])
             

              return plot_summed_condition_name, plot_raw_cor, plot_p_adj, module_id
            print(conditions_table)

            p_summed_condition_name = pd_cor_graphs(element_id)[0]
            p_raw_cor = pd_cor_graphs(element_id)[1]
            p_p_adj = pd_cor_graphs(element_id)[2]

            p_df = pd.DataFrame(list(zip(p_summed_condition_name, p_raw_cor,p_p_adj)), 
                    columns=['summed_condition_name','raw_correlation_score', 'adjusted_p_value'])
            


            




        

            conditions_plot = px.scatter(p_df, x='summed_condition_name', y='raw_correlation_score', color='adjusted_p_value',
                              title="Raw correlation score for each summed condition")
            
         
            
            plot_cond_div = pt.offline.plot(conditions_plot, auto_open = False, output_type="div")
             
            context = {
              'ni_data_nameid':ni_data_nameid,
              'ni_data_type':ni_data_type,
              'ni_data_text':ni_data_text,
              'element_id':element_id,
              'form_request':form_request,
              'request_denomer':request_denomer,
              'ni_mm':ni_mm,   
              'nodes_zip': nodes_zip,
              'all_nodes': all_nodes,
              'ez': edge_zip,
              's_nodes': s_nodes,
              'ned': ned,
              'plot_cond_div': plot_cond_div,
            
              'conditions_table': conditions_table, 
            }
          
          
          
          
          
          
          
# Element id is non type, error handling          
          else:
            context = {
              'ni_data_nameid': ni_data_nameid,
              'ni_data_type': ni_data_type,
              'ni_data_text': ni_data_text,
              'element_id':element_id,
              'form_request':form_request,
              'request_denomer':request_denomer,
              'ni_mm':ni_mm,

              

              }

#> Location search
      else:
        request_denomer = 'not_request'

        message = 'This is a search using an elements location, handle separatley'
        context= {
          'message':message,
          'request_denomer':request_denomer,

        }




# form validity  
    else: 
         print('not valid')
         context= {}


# method:POST          
  else: 
    print('not POST')
    context= {}  
  return render(request, 'Results/NetworkHunt_results.html', context)
