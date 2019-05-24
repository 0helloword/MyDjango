#M 模型，数据存取层，负责业务对象和数据库对象
#lib/models.py

from django.db import models

class Book(models.Model):
	name=models.CharField(max_length=200)
	author=models.CharField(max_length=100)
	pub_house=models.CharField(max_length=200)
	pub_date=models.DateTimeField('data published')
	
