"""
File: DataDossier/forms.py

Date: 020.09.2023
Function: create the form displayed on the template front end
Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
Make use of django functionalities to automate creation of html request form
------------------------------------------------------------------------------------------------------------------------
"""
from django import forms 
from turtle import textinput
from typing import Text



id_name_choices = [
  ('name', 'element name'),
  ('id', 'element id')
]


dummy_choices = [
  ('test1', 'test 1'),
  ('test2', 'test 2')
]


element_type_choices_nonloc = [
  ('Srna','sRNA'),
  ('Cds','CDS'),
  ('Utr','UTR'),
  ('Annotated_ncrna','Annotated ncRNA'),
]

mm_choices = [
  (0.9, '0.9'),
  (0.8, '0.8'),
  (0.7, '0.7'),
  (0.6, '0.6'),
  (0.5, '0.5'),
  (0.4, '0.4'),
]

raw_cor_choices = [
  (1, 'All associated'),
  (0.5, 'Strongly correlated'),
  (0, 'Weakly correlated'),
]

class NH_nameid_form(forms.Form):

  ui_element = forms.ChoiceField(choices= id_name_choices, label='Element id or name', widget=forms.RadioSelect)

  ui_type= forms.ChoiceField(choices= element_type_choices_nonloc, label='Genome element type', widget=forms.RadioSelect)
    
  ui_text_srna= forms.CharField(label='Text to search', max_length=50, required=False,  widget=forms.TextInput(attrs={'list':'ni_list_srna', }))
  
  ui_text_utr= forms.CharField(label='Text to search', max_length=50, required=False, widget=forms.TextInput(attrs={'list':'ni_list_utr', }))
  
  ui_text_cds= forms.CharField(label='Text to search', max_length=50, required=False, widget=forms.TextInput(attrs={'list':'ni_list_cds', }))
  
  ui_text_ancrna= forms.CharField(label='Text to search', max_length=50, required=False, widget=forms.TextInput(attrs={'list':'ni_list_ancrna', }))

  ui_mm = forms.ChoiceField(choices= mm_choices, label='Module match score')

  ui_raw_cor = forms.ChoiceField(choices= raw_cor_choices, label='Correlation strength') 
