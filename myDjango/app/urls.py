from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    path('add/', views.add, name='add')
    # path('',views.wel_ind),
    # path('list/',views.list),
    # path('toAdd/',views.toAdd),
    # path('add/',views.add),
    # path('toEdit/',views.toEdit),
    # path('edit/',views.edit),
 ]