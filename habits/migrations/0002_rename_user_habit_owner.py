# Generated by Django 3.2.21 on 2023-11-23 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='user',
            new_name='owner',
        ),
    ]