# Generated by Django 2.0 on 2017-12-24 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories_app.Story')),
            ],
        ),
    ]