from django.shortcuts import render
from multiprocessing import context
from django.db import connection

from django.db.models import Q
from django.views import View

from .forms import DD_nameid_form
from .models import Modules, ModuleCorrelation, Elements, Relations, Samples, GrowthConditions, GoTerms, Srna, Utr, AnnotatedNcrna, Cds


# Create your views here.
def DataDossier_homepage(request):
  

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

  ni_form= DD_nameid_form()

  context = {
    'ni_form' : ni_form,
    #'suggestions_zip': suggestions_zip,
    'suggestions_annotatedncrna' : suggestions_annotatedncrna,
    'suggestions_cds' : suggestions_cds,
    'suggestions_utr' : suggestions_utr,
    'suggestions_srna' : suggestions_srna,
    

  }
  return render(request, 'DataDossier.html', context)




def DataDossier_results(request):
  ni_form = DD_nameid_form(request.POST)
  
  if request.method == 'POST' :
    print('Method is POST')
    ni_form = DD_nameid_form(request.POST)
    #for i in ni_form:
      #print(i)

     #if 'dd_ni_form_submit' in request.POST:
      #print('query with element name or id')
    if ni_form.is_valid() :
        print('form is valid')

        ni_data_nameid = str(ni_form.cleaned_data['ui_element'])
        ni_data_type = str(ni_form.cleaned_data['ui_type'])
        ni_data_text_raw = [ni_form.cleaned_data['ui_text_srna']] + [ni_form.cleaned_data['ui_text_utr']] + [ni_form.cleaned_data['ui_text_cds']] + [ni_form.cleaned_data['ui_text_ancrna']]
     
        ni_data_text = ''.join(list(filter(None, ni_data_text_raw)))
       
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

        if element_id != 'e':
          def return_from_principle_table(element_id,ni_data_type):

            if ni_data_type == 'Srna':
              principle_rows = Srna.objects.filter(srna_element_id=element_id).values()
            elif ni_data_type == 'Utr':
              principle_rows = Utr.objects.filter(utr_element_id=element_id).values()
            elif ni_data_type == 'Cds':
              principle_rows = Cds.objects.filter(cds_element_id=element_id).values()
            elif ni_data_type == 'Annotated_ncrna':
              principle_rows = AnnotatedNcrna.objects.filter(annotated_ncrna_element_id=element_id).values()
       
            return principle_rows
          
          primary_level_info = return_from_principle_table(element_id,ni_data_type)[0]
          
          def sequence_length(element_id, ni_data_type):

            if ni_data_type != 'Cds':
              if ni_data_type != 'Annotated_ncrna':
                if ni_data_type == 'Srna':
                  seq_start = int(Srna.objects.filter(srna_element_id=element_id).values_list('seq_start', flat=True)[0])
                  seq_end = int(Srna.objects.filter(srna_element_id=element_id).values_list('seq_end', flat=True)[0])
                  sequence_length_calc = str(seq_end - seq_start)

                else: 
                  seq_start = int(Utr.objects.filter(utr_element_id=element_id).values_list('seq_start', flat=True)[0])
                  seq_end = int(Utr.objects.filter(utr_element_id=element_id).values_list('seq_end', flat=True)[0])
                  sequence_length_calc = str(seq_end - seq_start)
              else:
                sequence_length_calc = ''

            else:
              sequence_length_calc = ''


            return sequence_length_calc
          
          sequence_length_return = sequence_length(element_id, ni_data_type)

          def return_module_related_data(element_id):
            module_id = Relations.objects.filter(element_id=element_id).values_list('module_id',flat=True)[0]
            mm = Relations.objects.filter(element_id=element_id).values_list('module_match_score',flat=True)[0]

            strongest_cor = ModuleCorrelation.objects.filter(module_id=module_id).order_by('raw_cor').values()[:5]
            weakest_cor = ModuleCorrelation.objects.filter(module_id=module_id).order_by('-raw_cor').values()[:5]
            module_data  = Modules.objects.filter(module_id=module_id).values()[0]

            return strongest_cor, weakest_cor, mm, module_data
          
          strongest_cor_data = return_module_related_data(element_id)[0]
          weakest_cor_data = return_module_related_data(element_id)[1]
          mm_data = return_module_related_data(element_id)[2]
          module_data_data = return_module_related_data(element_id)[3]


          def gene_info(element_id):
            if ni_data_type != ('Cds' or 'Annotated_ncrna'):
              if ni_data_type == 'Srna':
                gene_id =   [i for i in Srna.objects.filter(srna_element_id=element_id).values_list('gene_element_id', flat=True)]
                              
                if gene_id[0] != None:
                  cds_data = Cds.objects.filter(cds_element_id=gene_id).values()
                  gene_data_zip = zip(cds_data)
                else:
                  
               
                  gene_data_zip = 'e'

              else:
                up_gene_id = Utr.objects.filter(utr_element_id=element_id).values_list('upstream_gene_element_id', flat=True)[0]
                print(up_gene_id)
                down_gene_id = Utr.objects.filter(utr_element_id=ni_data_text).values_list('downstream_gene_element_id', flat=True)[0]
                print(down_gene_id)


                up_cds_data = Cds.objects.filter(cds_element_id=up_gene_id).values()
                down_cds_data = Cds.objects.filter(cds_element_id=down_gene_id).values()
                gene_data_zip = zip( up_cds_data, down_cds_data)
              
              
                
            else:
             
              gene_data_zip = 'e'
             
            return gene_data_zip
          

          gene_data = gene_info(element_id)

          print(gene_data)

          
          context = {
            'ni_data_nameid': ni_data_nameid,
            'ni_data_type': ni_data_type,
            'ni_data_text': ni_data_text,
            'element_id':element_id,
            'primary_level_info':primary_level_info,
            'sequence_length_return':sequence_length_return,
            'strongest_cor_data':strongest_cor_data,
            'weakest_cor_data':weakest_cor_data,
            'mm_data':mm_data,
            'module_data_data':module_data_data,
            'gene_data':gene_data,




            
            } 
        


        else:
         
          context = {
            'ni_data_nameid': ni_data_nameid,
            'ni_data_type': ni_data_type,
            'ni_data_text': ni_data_text,
            'element_id':element_id,
            }

      
    else: 
         print('not valid')
         context= {}
        
   # else:
       #print('not in request POST')
          
  else: 
    print('not POST')
    context= {}
  return render(request, 'Results/DataDossier_results.html', context)

       
        
