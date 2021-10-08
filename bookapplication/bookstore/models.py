from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    copies=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.book_name