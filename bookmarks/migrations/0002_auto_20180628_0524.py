# Generated by Django 2.0.6 on 2018-06-28 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='category',
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='description',
        ),
    ]
