#-*-coding:utf-8-*-

from django.urls import path
from . import views

app_name='learn'
urlpatterns=[
	path('people_dict/',views.people_dict,name='people_dict'),
	path('ajax_list/',views.ajax_list,name='ajax_list'),
	path('ajax_dict/',views.ajax_dict,name='ajax_dict'),
	path('home',views.home,name='home'),
	path('add2/<int:a>/<int:b>/',views.add2,name='add2'),
	path('add/',views.add,name='add'),
	]