# from django.urls import path,include
from django.conf.urls import url
from . import  views

urlpatterns = [
    # path('admin/',admin.site.urls),
    url(r'^csdnFri/',views.csdnFri),
 ]