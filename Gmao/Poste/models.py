from django.db import models
from DirectCompany.models import DirectCompany
# Create your models here.
class Poste(models.Model):
    created_at =  models.DateTimeField(auto_now_add=True,auto_now=False)
    direct_company = models.ForeignKey(DirectCompany,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    regie = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=4, decimal_places=2)
    lng = models.DecimalField(max_digits=4, decimal_places=2)