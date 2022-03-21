from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def welcome(request):

    return HttpResponse("hello Django!")

def index(request):

    return render(request,'/index.html',{'form':list})
