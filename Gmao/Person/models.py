from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Person(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    functionality = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)

