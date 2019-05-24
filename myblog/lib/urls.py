#URL分发器的作用是将页面请求分发给不同的视图(View)处理，视图再调用相应的模型(Model)和模板(Template)。

from django.urls import path
from . import views

app_name='lib'
urlpatterns=[
	path('',views.index,name='index'),
	path('detail/',views.detail,name='detail'),
	path('addBook/',views.addBook,name='addBook'),
	path('delBook/<int:book_id>',views.deleteBook,name='delBook'),
	path('searchBook/',views.searchBook,name='searchBook'),
	path('editBook/',views.editBook,name='editBook'),
	]