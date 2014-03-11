from django.db import models
from registration.models import User


class User_Profile(models.Model):
    avatar = models.ImageField(upload_to='static/media/')
    total_bounty_points = models.PositiveIntegerField()
    usr = models.OneToOneField(User)

class Cohab(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length= 200)
    description = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to='static/media/')
    usr = models.ManyToManyField(User_Profile)

class List(models.Model):
    name = models.CharField(max_length=75)
    total_bounty_points = models.PositiveIntegerField()
    cohab = models.ForeignKey(Cohab)

class List_Item(models.Model):
    name = models.CharField(max_length=75)
    bounty_points = models.PositiveIntegerField()
    list = models.ForeignKey(List)


