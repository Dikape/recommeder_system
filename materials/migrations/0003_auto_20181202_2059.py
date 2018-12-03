# Generated by Django 2.1.3 on 2018-12-02 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='redactor_mark',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
