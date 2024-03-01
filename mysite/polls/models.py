import datetime

from django.db import models
from django.utils import timezone


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.name



