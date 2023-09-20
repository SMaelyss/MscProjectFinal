"""
File: ScientificBasis/urls.py

Date: 16.07.2023
Description: sb app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views


urlpatterns = [
  path('', views.ScientificBasis, name='ScientificBasis'),
]