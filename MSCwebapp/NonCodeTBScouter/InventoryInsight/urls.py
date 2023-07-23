"""
Description: ii app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views
from unicodedata import name


from Home.views import homepage
from InventoryInsight.forms import IIForm


urlpatterns = [
  path('', views.InventoryInsight_homepage, name='InventoryInsight_homepage'),
  path('InventoryInsight_results', views.InventoryInsight_results, name='InventoryInsight_results'),
]
