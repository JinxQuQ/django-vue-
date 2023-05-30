from django.db import models


# from __future__ import unicode_literals

# Create your models here.

class Book(models.Model):
    objects = None
    book_name = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name
