from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.views.decorators import csrf
from app.models import Test

list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def welcome(request):

    return HttpResponse("hello Django!")

def index(request):

    name = request.POST.get('name',None)
    password = request.POST.get('password',None)
    data = {'name':name, 'password':password}
    list.append(data)

    return render(request,'myDjango/index.html',{'form':list})

def save_data(request):
    data={}
    if request.POST:
        if 'add' in request.POST:
            test1 = Test(name=request.POST['add_data'])
            test1.save()
            data['result']='数据添加成功'
        if 'update' in request.POST:
            ID  = int(request.POST['update_data'])
            test1 = Test.objects.get(id=ID)
            test1.name='change'
            test1.save()
            data['result']='数据修改成功'
        if 'delete' in request.POST:
            ID = int(request.POST['delete_data'])
            test1=Test.objects.get(id=ID)
            test1.delete()
            data['result']='删除数据成功'
        if 'selete' in request.POST:
            ID = int(request.POST['select_data'])
            test1=Test.objects.get(id=ID)
            data['result']=test1.name

    return render(request, 'myDjango/save_data.html',data)