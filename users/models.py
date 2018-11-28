from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female')
)

class FbInfo(models.Model):
    home_address = models.CharField(max_length=100)
    home_adderess_lat = models.CharField(max_length=100)
    home_address_lng = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_lat = models.CharField(max_length=100)
    location_lng = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICE)
    friends_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
