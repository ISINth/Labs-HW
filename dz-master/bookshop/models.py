from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
	name=models.CharField(max_length=100, default='2')
	author=models.CharField(max_length=100, default='А вот тут самая изысканная шведская мебель')
	cover=models.CharField(max_length=7, choices=(("5","5"), ("4","4"), ("3","3"), ("2","2") , ("1","1")),default="3")
	number=models.IntegerField(default='1')
	img=models.ImageField(upload_to="bookshop/static/", default='1')
	desc=models.TextField(default='1')

	def __str__(self):
		return self.name

class Book_User(models.Model):
	user=models.CharField(max_length=200)
	book=models.IntegerField()
	number=models.IntegerField()