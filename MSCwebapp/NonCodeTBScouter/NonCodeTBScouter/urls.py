"""
URL configuration for NonCodeTBScouter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from argparse import Namespace
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Howto/', include('HowTo.urls')),
    path('InventoryInsight/', include('InventoryInsight.urls')),
    path('DataDossier/', include('DataDossier.urls')),
    path('NetworkHunt/', include('NetworkHunt.urls')),
    path('ResourceGateway/', include('ResourceGateway.urls')),
    path('ScientificBasis/', include('ScientificBasis.urls')),




]
