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

II_choices = [
  ('r_modules', 'Modules'),
  ('r_elements', 'Elements'),
  ('r_samples', 'Samples'),
  ('r_goterms', 'GO terms'),
]

class IIForm(forms.Form):
    #IIdata = forms.ChoiceField(choices= II_choices, label= 'Data request')
    IIdata = forms.ChoiceField(widget=forms.RadioSelect, choices=II_choices)