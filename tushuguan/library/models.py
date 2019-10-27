from django.db import models

# Create your models here.

class book(models.Model):
    bookId = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    publication = models.CharField(max_length=30)
    press = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    remove = models.BooleanField(default=False)
    class Meat:
        db_table = "book"