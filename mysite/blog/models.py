# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(u'文章分类', max_length=40)
    
    class Meta:
	ordering = ['-id']

    def __unicode__(self):
	return self.name

class Post(models.Model):
    title = models.CharField(u'标题', max_length=128)
    author = models.ForeignKey(User, verbose_name=u'作者')
    category = models.ForeignKey(Category, verbose_name=u'类别')
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(u'内容')


    class Meta:
	ordering = ['-id']

    def __unicode__(self):
	return self.title
# Create your models here.
