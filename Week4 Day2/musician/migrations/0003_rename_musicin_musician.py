# Generated by Django 5.1 on 2024-08-23 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('musician', '0002_alter_musicin_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Musicin',
            new_name='Musician',
        ),
    ]
