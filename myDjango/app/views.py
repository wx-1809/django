from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def welcome(request):

    return HttpResponse("hello Django!")