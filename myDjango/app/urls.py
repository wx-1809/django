from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('admin/',admin.site.urls),
    path('list/',views.list),
    path('toAdd/',views.toAdd),
    path('add/',views.add),
    path('toEdit/',views.toEdit),
    path('edit/',views.edit),
 ]