from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article,Column,Account
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse
import tkinter.messagebox #弹窗库
from tkinter import *
from django.contrib import messages

def index(request):
#     return HttpResponse(u'欢迎来自自强学堂学习Django')
    #展示所有栏目及链接
#     columns=Column.objects.all()
#     return render(request,'index.html',{'columns':columns})
    home_display_columns=Column.objects.filter(home_display=True)#首页仅显示home_display为True的栏目
    nav_display_columns=Column.objects.filter(nav_display=True)#导航栏仅显示nav_display为True的栏目
    return render(request,'index.html',{
        'home_display_columns':home_display_columns,
        'nav_display_columns':nav_display_columns,                                
                                        })
    
def login(request):
    return render(request,'login.html')
    
def register(request):
    return render(request,'register.html')

def userlogin(request):    
    m = Account.objects.get(accountName=request.POST['username'])
    
    if m.password != request.POST['password']:
        messages.error(request, '用户名或密码不正确')
        return HttpResponseRedirect(reverse('login'))     
    else:
        messages.success(request, '登录成功')
        return HttpResponseRedirect(reverse('index'))

def addUser(request):
    if request.method=='POST':
        temp_name=request.POST['username']
        temp_password=request.POST['password']
        temp_email=request.POST['email']

    from django.utils import timezone
    account_list=Account.objects.filter(accountName=temp_name)
    if len(account_list)>=1:
        messages.warning(request, '用户已存在')
        return HttpResponseRedirect(reverse('register'))
    else:
        temp_accountName=Account(accountName=temp_name,password=temp_password,email=temp_email,create_time=timezone.now())
        temp_accountName.save()
        messages.success(request, '注册成功')
        return HttpResponseRedirect(reverse('login'))

def column_detail(request,column_slug):
#     return HttpResponse('column slug:'+column_slug)
    column=Column.objects.get(slug=column_slug)
    return render(request,'news/column.html',{'column':column})

def article_detail(request,article_slug):
#     return HttpResponse('article slug:'+article_slug)
    article=Article.objects.get(slug=article_slug)
    return render(request,'news/article.html',{'article':article})

from django.shortcuts import render
 
def p1(request):
    return render(request,"p1.html")
 
def p2(request):
    if request.method == "GET":
        return render(request,"p2.html")
    elif request.method == "POST":
        city =request.POST.get("city")
        print(city)
        return render(request,"popup_response.html",{"city":city})