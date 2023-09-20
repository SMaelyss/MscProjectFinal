"""
File: InventoryInsight/views.py

Date: 020.09.2023
Function: Display onto front end, form to obtain table view of the database layer of the website.
Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
functions:
  InventoryInsight_homepage renders the request form.
  InventoryInsight_results takes the request from the form and retrieves the requested data from the database and passes it to the InventoryInsight_results.html.
------------------------------------------------------------------------------------------------------------------------
"""

from django.shortcuts import render
from multiprocessing import context

from django.db import connection

# import the form
from InventoryInsight.forms import IIForm


# Import the model classes (tables from database)
from .models import Modules, ModuleCorrelation, Elements, Relations, Samples, GrowthConditions, GoTerms


# Create your views here.
def InventoryInsight_homepage(request):
  form = IIForm()
  return render(request, 'InventoryInsight.html',  {'form': form})


def InventoryInsight_results(request):
  form = IIForm(request.POST) # return the request from  the form
  
  if request.method == 'POST':
     form = IIForm(request.POST)
     print('Method is POST') # Is printed in temrinal for testing purposes
     if form.is_valid(): # Validating the form
      IIdata = form.cleaned_data['IIdata'] # Clean the data sent through from the form
      print(IIdata) # Print post request in temrinal for testing purposes

#Modules      
      if IIdata == 'r_modules':
        # Obtain data from models related to modules
        m_all =  Modules.objects.all() # objects.all obtains everything in model table
        mc_all = ModuleCorrelation.objects.all() 
        mc_summed_condition_name = ModuleCorrelation.objects.values_list('summed_condition_name', flat=True) 
        # summed condition name is foreign key thus must be obtained as a values list to avoid each object having a pre-fix.
        mc_module = ModuleCorrelation.objects.values_list('module', flat=True) 
        # A foreign key column, flat=True makes sure only object is returned without model name prefix or data type pre-fix
        mc_table_zip = zip(mc_all, mc_summed_condition_name, mc_module) # Create a zip to iterated a for loop in the html page
        #context dict to be called dynamically in the html webpage
        
        
        m_names = Modules.objects.values_list('module_id', flat=True) 
        m_enrich_utr_qval = Modules.objects.values_list('enrich_utr_qval', flat=True) 
        pandas_enrichutr_zip = zip(m_names, m_enrich_utr_qval)
        
        context ={
          'm_all':m_all,
          'mc_table_zip': mc_table_zip,
          'm_enrich_utr_qval': m_enrich_utr_qval,
          'm_names': m_names,
          'pandas_enrichutr_zip': pandas_enrichutr_zip,

          'IIdata': IIdata,
        }

       


#Samples
      elif IIdata == 'r_samples':
        s_all = Samples.objects.all()
        s_full_con = Samples.objects.values_list('full_condition', flat=True)
        #res = Samples.objects.filter(sample_id__in=s_all)
        s_table_zip = zip(s_all, s_full_con)


        gc_full_condition_name = GrowthConditions.objects.values_list('full_condition_name', flat=True)
        gc_full_condition_id = GrowthConditions.objects.values_list('full_condition_id', flat=True)
        gc_table_zip = zip(gc_full_condition_name, gc_full_condition_id)
        context ={
          's_table_zip': s_table_zip,
          'gc_table_zip':gc_table_zip,
          'IIdata': IIdata,
        }

#Elements
      elif IIdata == 'r_elements':
        e_id = Elements.objects.values_list('element_id', flat=True)
        e_type = Elements.objects.values_list('element_type', flat=True)
        e_table_zip = zip(e_id, e_type) 

        r_all = Relations.objects.all()
        r_element = Relations.objects.values_list('element', flat=True)
        r_module = Relations.objects.values_list('module', flat=True)
        r_table_zip = zip(r_all, r_element, r_module )

        context ={
          'e_table_zip':e_table_zip,
          'r_table_zip':r_table_zip,
          'IIdata': IIdata,
        }

#Go terms
      else:
        gt_all  = GoTerms.objects.all()
        context ={
          'gt_all':gt_all,
          'IIdata': IIdata,
        }



        

        
      print(connection.queries)

    
  else:
    print('not POST') # if the request is not post - error handeling, this will not appear on the webpage. 
    # Dynamic context for the wepage to be added later.
  
  return render(request, 'Results/InventoryInsight_results.html', context)