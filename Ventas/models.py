from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.FloatField()
