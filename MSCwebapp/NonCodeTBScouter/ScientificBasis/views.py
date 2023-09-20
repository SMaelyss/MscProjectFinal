"""
File: ScientificBasis/views.py

Date: 020.09.2023
Function: Display onto front end, ScientificBasis.html.
Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
functions:
  ScientificBasis renders ScientificBasis.html.
------------------------------------------------------------------------------------------------------------------------
"""

from django.shortcuts import render

# Create your views here.
def ScientificBasis(request):
  return render(request, 'ScientificBasis.html')