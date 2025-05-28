# product/models/Product.py

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)

