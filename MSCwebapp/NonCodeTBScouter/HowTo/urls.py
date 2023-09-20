"""
File: HowTo/urls.py

Date: 029.05.2023
Description: HowTo app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views


urlpatterns = [
  path('', views.HowTo, name='HowTo'),
]
