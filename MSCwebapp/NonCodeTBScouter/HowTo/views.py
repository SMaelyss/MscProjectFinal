"""
File: HowTo/views.py

Date: 020.09.2023
Function: Display onto front end, HowTo.html .
Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
functions:
  HowTo renders HowTo.html.
------------------------------------------------------------------------------------------------------------------------
"""

from django.shortcuts import render

# Create your views here.

def HowTo(request):
  return render(request, 'HowTo.html') 