from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from materials.models import UserMark
import numpy as np


GENDER_CHOICE = (
    (1, 'Male'),
    (0, 'Female')
)


class FbInfo(models.Model):
    home_address = models.CharField(max_length=100)
    home_address_lat = models.CharField(max_length=100)
    home_address_lng = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_lat = models.CharField(max_length=100)
    location_lng = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICE)
    friends_count = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_vector(self, materials):

        user_vector = [
            self.user.fbinfo.home_address_lat,
            self.user.fbinfo.home_address_lng,
            self.user.fbinfo.location_lat,
            self.user.fbinfo.location_lng,
            self.user.fbinfo.location_lng,
            self.user.fbinfo.age,
            self.user.fbinfo.gender + 10,
            self.user.fbinfo.friends_count,
        ]
        for material in materials:
            try:
                mark = self.user.usermark_set.get(material=material).mark
            except UserMark.DoesNotExist:
                mark = 0
            user_vector.append(mark)
        print(f'prepare user - {self.user.id}')
        return np.asarray(user_vector)


class FacebookTokens(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
