# Generated by Django 5.1 on 2024-09-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('posts', '0002_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
