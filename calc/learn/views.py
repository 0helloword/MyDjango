from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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


def ajax_list(request):
	a=list(range(100))
	return JsonResponse(a,safe=False)

def ajax_dict(request):
	name_dict= {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
	return JsonResponse(name_dict)

def people_dict(request):
	person_dict=[
    {"name":"xiaoming", "age":20},
    {"name":"tuweizhong", "age":24},
    {"name":"xiaoli", "age":33},
]
	return JsonResponse(person_dict)



