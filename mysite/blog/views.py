from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def index(request):
	return render(request,'index.html')

def login(request):
    m = User.objects.get(name=request.POST['username'])
   
    if m.password == request.POST['password']:
        request.session['name'] = m.name
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")
   
         
def logout(request):
    try:
        del request.session['name']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
   
def comment(request):#如果已评论不允许再评论，反之更新评论
	newComment=request.POST['comment']
	m=User.objects.get(name=request.POST['username'])
	if m.comment!='123':
		return HttpResponse("you've already commented")
	else:	
		m.comment=newComment	
		m.save()
		return HttpResponse('thanks for your comment!')