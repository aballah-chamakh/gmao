from django.db import models
from Person.models import Person 
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class AffiliateCompany(models.Model):
    persons = models.ManyToManyField(Person)
    name = models.CharField(max_length=255,default="")
    address = models.CharField(max_length=255,default="")
    city = models.CharField(max_length=255,default="")
    country = models.CharField(max_length=255,default="")
    email = models.EmailField(max_length=255,default="")
    tel = models.CharField(max_length=255,default="")
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self):
        return self.name 

@receiver(pre_delete, sender=AffiliateCompany)
def pre_delete_person(sender, instance,**kwargs):
    persons = instance.persons.all()
    for person in persons : 
        person.delete()


