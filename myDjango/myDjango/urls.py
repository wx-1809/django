"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from app import views


def wel_ind(req):
    return render(req, 'templates/wel_ind.html')

urlpatterns = [
    path('welcome/', views.welcome),
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('save_data/',views.save_data),
    path('db_handle/',views.db_handle),
    path('wel_ind/',wel_ind),
    path('app/',include('app.urls')),
    # url(r'^app/',include('app.urls')),
]
