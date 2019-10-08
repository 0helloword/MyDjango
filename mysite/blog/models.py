from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	
	def __str__(self):
		return self.title
	
class User(models.Model):
	name=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	has_comment=models.CharField(default='Y',max_length=1)
	comment=models.CharField(default='123',max_length=50)
	
	def __str__(self):
		return self.name
		
