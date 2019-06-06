from django.shortcuts import render
from django.http import HttpResponse

def add(request):
	a=request.GET['a']
	b=request.GET['b']
	c=int(a)+int(b)
	return HttpResponse(str(c))
	
def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))
	
def home(request):
	string1=u"这是字符串1"
	string2=u"这是字符串2"
	list=['html','css','jquery','python']
	dict={'site':u'自强学堂','content':u'各种IT教程'}
	list2=map(str,range(100))
	list3=[]
	var=45
	return render(request,'home.html',{'string1':string1,'string2':string2,'list':list,'dict':dict,'list2':list2,'list3':list3,'var':var})