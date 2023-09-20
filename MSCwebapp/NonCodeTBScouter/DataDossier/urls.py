"""
File: DataDossier/urls.py

Date: 029.05.2023
Description: DD app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views
from unicodedata import name


from Home.views import homepage
from DataDossier.forms import DD_nameid_form


urlpatterns = [
  path('', views.DataDossier_homepage, name='DataDossier_homepage'),
  path('DataDossier_results', views.DataDossier_results, name='DataDossier_results'),
]
