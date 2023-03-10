"""Ezra_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= 'index'),
    path('services/', views.services, name= 'services'),
    path('contactcopy/', views.contactcopy, name= 'contactcopy'),
    path('about/', views.about, name= 'about'),
    path('rhino_index/', views.rhino_index, name='rhino_index'),
    path('rhino_about/', views.rhino_about, name='rhino_about'),
    path('rhino_contact/', views.rhino_contact, name= 'rhino_contact'),
    path('rhino_project/', views.rhino_project, name= 'rhino_project')
]
#Dont forget the backslash
