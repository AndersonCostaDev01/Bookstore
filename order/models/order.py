# Model Order

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ManyToManyField('product.Product', blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)