# Generated by Django 3.2.6 on 2021-08-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_applies_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='applies',
            name='applied_to',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
