# Generated by Django 4.1.2 on 2022-11-30 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatubeapp', '0006_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='categoryid',
        ),
    ]