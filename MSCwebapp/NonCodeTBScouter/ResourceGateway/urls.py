"""
File: ResourceGateway/urls.py

Date: 16.07.2023
Description: rg app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views


urlpatterns = [
  path('', views.ResourceGateway, name='ResourceGateway'),
]