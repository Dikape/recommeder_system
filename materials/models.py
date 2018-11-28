from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

class Material(models.Model):
    title_original = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    technical_description = models.CharField(max_length=2000)
    material_type = models.ForeignKey('MaterialType', on_delete=models.CASCADE)
    average_mark = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    redactor_mark = models.IntegerField(
        models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)]))


class MaterialTitleTranslate(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    language = models.CharField(max_length=32)
    translate = models.CharField(max_length=255)


class MaterialType(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    image = models.ImageField()
    counter = models.IntegerField()


class RedactorReview(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Advertisement(models.Model):
    picture = models.ImageField()
    text = models.CharField(max_length=5000)
    reference = models.CharField(max_length=5000)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class UserMark(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    redactor_mark = models.IntegerField(
        models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)]))
    is_from_fb = models.BooleanField(default=False)


class UserComment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=5000)
