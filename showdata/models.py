from django.db import models

# Create your models here.

class house(models.Model) :
    title = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)
    place = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    per_meter =  models.FloatField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)

class newhouse(models.Model):
    title = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)
    place = models.CharField(max_length=200, null=True, blank=True)
    # price = models.CharField(max_length=15, null=True, blank=True)
    per_meter = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)

class hirehouse(models.Model):
    title = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)
    place = models.CharField(max_length=10, null=True, blank=True)
    price = models.CharField(max_length=15, null=True, blank=True)
    per_meter = models.CharField(max_length=15, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)