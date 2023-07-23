from django.shortcuts import render
from multiprocessing import context
from django.db import connection

from django.db.models import Q
from django.views import View

from .forms import NH_nameid_form
from .models import Modules, ModuleCorrelation, Elements, Relations, Samples, GrowthConditions, GoTerms, Srna, Utr, AnnotatedNcrna, Cds



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
# method:POST           
  if request.method == 'POST' :
    print('Method is POST')
    ni_form = NH_nameid_form(request.POST)
    form_request = (request.POST)
# form validity
    if ni_form.is_valid() :
      print('form is valid')
# (Location) or (Name and ID)
      if 'dd_ni_submit' in form_request:
          request_denomer = 'ni_request'

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
            context = {
              'ni_data_nameid':ni_data_nameid,
              'ni_data_type':ni_data_type,
              'ni_data_text':ni_data_text,
              'element_id':element_id,
              'form_request':form_request,
              'request_denomer':request_denomer,


            }
          else:
            context = {
              'ni_data_nameid': ni_data_nameid,
              'ni_data_type': ni_data_type,
              'ni_data_text': ni_data_text,
              'element_id':element_id,
              'form_request':form_request,
              'request_denomer':request_denomer,
              

              }


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
