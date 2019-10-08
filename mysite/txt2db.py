#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")

import django
if django.VERSION>=(1,7):
	django.setup()#否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
	
# def main():
# 	from blog.models import Blog
# 	f=open('oldblog.txt')
# 	for line in f:
# 		title,content=line.split('****')
# 		#Blog.objects.create(title=title,content=content)#每保存一条数据就执行一次sql
# 		Blog.objects.get_or_create(title=title,content=content)#避免重复导入数据，有就获取，没有就创建
# 	f.close()

def main():
	from blog.models import Blog
	f=open('oldblog.txt')
	BlogList=[]
	for line in f:
		title,content=line.split('****')
		blog=Blog(title=title,content=content)
		BlogList.append(blog)
	f.close()
	Blog.objects.bulk_create(BlogList)#bulk_create()是执行一条SQL存入多条数据，做会快很多
	
if __name__=="__main__":
	main()
	print("Done!")
	
	