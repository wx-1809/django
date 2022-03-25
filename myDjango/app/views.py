from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.views.decorators import csrf
from app.models import Test
from app import models

list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def welcome(request):

    return HttpResponse("hello Django!")

def index(request):

    name = request.POST.get('name',None)
    password = request.POST.get('password',None)
    data = {'name':name, 'password':password}
    list.append(data)

    return render(request,'index.html',{'form':list})

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

    return render(request, 'save_data.html',data)

def db_handle(request):
    """add number"""
    # models.UserInfo.objects.create(username='andy',password='123456', age=33)
    # dic = {"username":"christ","password":"123456","age":33}
    # models.UserInfo.objects.create(**dic)
    """#delete datanumber;"""
    # models.UserInfo.objects.filter(id=2).delete()
    """"update database;"""
    # models.UserInfo.objects.filter(id=1).update(age=18)

    # return HttpResponse('OK')

    """use html deal with databases:use file select data"""
    if request.method == "POST":
        models.UserInfo.objects.create(username=request.POST['username'],password=request.POST['password'],age=request.POST['age'])

    user_list_obj = models.UserInfo.objects.all()

    # return  render(request,'databases_deal.html',{'li':user_list_obj})
    return render(request, 'static_css.html', {'li': user_list_obj})

def csdnFri(request):
    data = models.Fri.objects.all()
    return render(request,'csdnFri.html',locals())
