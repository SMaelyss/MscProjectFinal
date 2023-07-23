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