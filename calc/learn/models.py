
from django.db import models

class Animal(models.Model):
    def __init__(self,name,sound):
        self.name=models.CharField(max_length=30)
        self.sound=models.CharField(max_length=30)

        
    def speak(self):
        print( 'the %s says "%s"'%(self.name,self.sound))

