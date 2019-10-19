from django.db import models

# Create your models here.
class Machine(models.Model):
    mid = models.CharField(max_length=4,primary_key=True)
    name = models.CharField(max_length=100)
    rent = models.DecimalField(max_digits=100, decimal_places=2)
    details = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    image = models.CharField(max_length=200)

class Tip(models.Model):
    tid = models.CharField(max_length=4, primary_key=True)
    desc = models.CharField(max_length=500)

class Stage(models.Model):
    sid = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    machines = models.ManyToManyField(Machine)
    image = models.CharField(max_length=200)
    tips = models.ManyToManyField(Tip, blank=True)

class Crop(models.Model):
    cid = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    stages = models.ManyToManyField(Stage)
    image = models.CharField(max_length=200)
    tips = models.ManyToManyField(Tip, blank=True)