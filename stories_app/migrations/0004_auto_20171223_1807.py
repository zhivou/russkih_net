# Generated by Django 2.0 on 2017-12-24 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories_app', '0003_auto_20171223_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='containerID',
        ),
        migrations.DeleteModel(
            name='Container',
        ),
    ]
