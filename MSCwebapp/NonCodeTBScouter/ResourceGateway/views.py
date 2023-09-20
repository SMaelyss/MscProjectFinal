"""
File: ResourceGateway/views.py

Date: 020.09.2023
Function: Display onto front end, ResourceGateway.html.
Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
functions:
  ResourceGateway renders ResourceGateway.html.
------------------------------------------------------------------------------------------------------------------------
"""


from django.shortcuts import render

# Create your views here.
def ResourceGateway(request):
  return render(request, 'ResourceGateway.html')
