# Generated by Django 3.2.6 on 2021-08-19 14:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210817_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrerlevel',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='max_experience',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='job',
            name='min_experience',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
