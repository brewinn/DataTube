# Generated by Django 4.1.2 on 2022-11-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datatubeapp', '0005_video_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoid', models.CharField(max_length=12)),
                ('tag', models.TextField()),
            ],
        ),
    ]
