from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def welcome(request):

    return HttpResponse("hello Django!")

def index(request):

    name = request.POST.get('name',None)
    password = request.POST.get('password',None)
    data = {'name':name, 'password':password}
    list.append(data)

    return render(request,'myDjango/index.html',{'form':list})
