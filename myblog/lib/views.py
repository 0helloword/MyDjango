#V 视图，负责业务逻辑，并在适当时候调用模型model和模板Template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	return HttpResponse("Hello,world!\n Welcome to django!")
	
def detail(request):
	book_list=Book.objects.order_by('-pub_date')[:5]#展示最新的5条记录
	context={'book_list':book_list}
	return render(request,'lib/detail.html',context)
	
def addBook(request):
	if request.method=='POST':
		temp_name=request.POST['name']
		temp_author=request.POST['author']
		temp_pub_house=request.POST['pub_house']
	
	from django.utils import timezone
	temp_book=Book(name=temp_name,author=temp_author,pub_house=temp_pub_house,pub_date=timezone.now())
	temp_book.save()
	
	return HttpResponseRedirect(reverse('lib:detail'))
	
def deleteBook(request,book_id):
	bookID=book_id
	Book.objects.filter(id=bookID).delete()
	return HttpResponseRedirect(reverse('lib:detail'))
	
def searchBook(request):
	if request.method=='POST':
		bookName=request.POST['name']
	book_list=Book.objects.filter(name__icontains=bookName)#名字中包含bookName并不区分大小写
	if book_list:	
		context={'book_list':book_list}
		return render(request,'lib/search.html',context)
	else:
		return render(request,'lib/notFound.html')
	
def editBook(request):
	if request.method=='POST':
		temp_name=request.POST['name']
		temp_author=request.POST['author']
		temp_pub_house=request.POST['pub_house']

	twz = Book.objects.get(name=temp_name)
	if twz:
		twz.author=temp_author
		twz.pub_house=temp_pub_house
		twz.save() 	
		return HttpResponseRedirect(reverse('lib:detail'))
	else:
		return render(request,'lib/notFound.html')
	
	
	
	


