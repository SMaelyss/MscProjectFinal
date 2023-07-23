"""
Description: nh app, url file
urls for the navigation functions

"""

from django.urls import path

from . import views
from unicodedata import name


from Home.views import homepage
from InventoryInsight.forms import IIForm


urlpatterns = [
  path('', views.NetworkHunt_homepage, name='NetworkHunt_homepage'),
  path('NetworkHunt_results', views.NetworkHunt_results, name='NetworkHunt_results'),

]
