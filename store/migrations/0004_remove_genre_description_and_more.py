# Generated by Django 5.0.4 on 2024-05-05 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_genre_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='meta_title',
        ),
    ]
