from django.db import models

# Create your models here.
class Order(models.Model):
    order_name = models.CharField(max_length=200)