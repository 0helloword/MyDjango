# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django.urls import reverse

class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)#使用db_index=True对slug建立索引
    intro = models.TextField('栏目简介', default='')

    nav_display=models.BooleanField('导航显示',default=False)
    home_display=models.BooleanField('首页显示',default=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):#获取网址的功能
        return reverse('column',args=(self.slug,))#reverse反解析url以直接访问其它视图方法

    class Meta:#class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准。
        verbose_name = '栏目'#verbose_name给模型类起一个更可读的名字一般定义为中文
        verbose_name_plural = '栏目'#这个选项是指定，模型的复数形式是什么
        ordering = ['name'] #按照哪个栏目排序


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')#一篇文章属于多个栏目

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.CharField('作者', blank=True, null=True,max_length=256)#在django2.0后，定义外键和一对一关系的时候需要加on_delete选项
#     content = models.TextField('内容', default='', blank=True)
    content=UEditorField('内容',height=300,width=1000,default=u'',blank=True,
                         imagePath="uploads/images/",toolbars='besttome',
                         filePath='uploads/files/')
    
    
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)#auto_now_add为添加时的时间，更新对象时不会有变动。
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)#auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article',args=(self.slug,))#注意args参数为元组,后面要加逗号
    
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

#新增登录注册功能，增加对应的用户表        
class Account(models.Model):
    accountName=models.CharField('用户名',max_length=256)
    password=models.CharField('密码',max_length=126)
    email=models.CharField('邮箱',max_length=256)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)#auto_now_add为添加时的时间，更新对象时不会有变动。

    def __str__(self):
        return self.accountName








