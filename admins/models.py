from django.db import models

# Create your models here.

class BusinessDetails(models.Model):
    year=models.IntegerField()
    field=models.CharField(max_length=300)
    investment=models.IntegerField()
    returnamount=models.IntegerField()
    profit=models.IntegerField()
    profitreason=models.CharField(max_length=1000)
    loss=models.IntegerField()
    lossreason=models.CharField(max_length=1000)
    currentissues=models.CharField(max_length=1000)
    strategy=models.CharField(max_length=100)
