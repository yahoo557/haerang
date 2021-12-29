from django.db import models

# Create your models here.

class Address(models.Model) :
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name