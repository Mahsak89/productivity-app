# Generated by Django 3.2.21 on 2023-09-21 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='startdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]