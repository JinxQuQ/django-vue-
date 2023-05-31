# from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)
    book_author = models.CharField(max_length=50,default="unknown")

    def __str__(self):
        return self.book_name



