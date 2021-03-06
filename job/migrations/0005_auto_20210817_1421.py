# Generated by Django 3.2.6 on 2021-08-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210817_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='career_level',
            field=models.ManyToManyField(blank=True, to='job.CarrerLevel'),
        ),
        migrations.AlterField(
            model_name='job',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='job.Category'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.ManyToManyField(blank=True, to='job.JobType'),
        ),
    ]
