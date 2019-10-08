"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoUeditor import urls 
from django.conf.urls import include,url
from news import views

urlpatterns = [
    url(r'^p1.html',views.p1),
    url(r'^p2.html', views.p2),
    url(r'^userlogin/',views.userlogin,name='userlogin'),
    url(r'^addUser/',views.addUser,name='addUser'),           
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^index/',views.index,name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$',views.column_detail,name='column'),
    url(r'^article/(?P<article_slug>[^/]+)/$',views.article_detail,name='article'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    path('admin/', admin.site.urls),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(
        settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
