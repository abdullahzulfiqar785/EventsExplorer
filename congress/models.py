from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

# Create your models here.
class Registration(models.Model):
    Category = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=4 , decimal_places=2)
    late_fee = models.DecimalField(max_digits=4 , decimal_places=2)

class Hotels(models.Model):
    image = models.ImageField(upload_to='static')
    title = models.CharField(max_length=255)
    description = models.TextField()
