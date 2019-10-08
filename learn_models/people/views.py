from django.shortcuts import render
from django.http import HttpRequest
import json

def home(request):
    list=['python','django','java']
    dict={'low':'1','middle':'2','high':'3'}
    return render(request,'home.html',{
                                       'list':json.dumps(list),
                                       'dict':json.dumps(dict)
                                       })
