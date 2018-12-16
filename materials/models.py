from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User


class Material(models.Model):
    image = models.ImageField(max_length=500)
    title_original = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    technical_description = models.CharField(max_length=2000)
    material_type = models.ForeignKey('MaterialType', on_delete=models.CASCADE)
    average_mark = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    redactor_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.title_original}'

    def calculate_average(self):
        pass

    def get_all_translates(self):
        pass


class MaterialTitleTranslate(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    language = models.CharField(max_length=32)
    translate = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.material}-{self.language}'


class MaterialType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.CharField(max_length=5000)
    image = models.ImageField()
    counter = models.IntegerField()

    def calc_counter(self):
        pass

    def __str__(self):
        return f'{self.title}'


class RedactorReview(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_author_full_name(self):
        pass

    def __str__(self):
        return f'{self.material} - {self.author}'


class Advertisement(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)
    reference = models.CharField(max_length=5000)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


    def __str__(self):
        return f'{self.material} - {self.title}'


class UserMark(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    redactor_mark = models.IntegerField(
        models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)]))
    is_from_fb = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.material} - {self.user}'


class UserComment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.material} - {self.user}'
