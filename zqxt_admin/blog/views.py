from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'index.html')
	
def add(request):
	a=request.GET['a']
	b=request.GET['b']
	return HttpResponse(str(int(a)+int(b)))
