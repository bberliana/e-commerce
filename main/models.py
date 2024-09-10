from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=255)
   