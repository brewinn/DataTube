from django.db import models

# Create your models here.


class Video(models.Model):
    videoid = models.CharField(max_length=12, primary_key=True)
    title = models.TextField()
    #views = models.IntegerField(null=True)
    #published = models.DateField(null=True)
    #duration = models.TextField(null=True)
    #tags = models.TextField(null=True)
    #likes = models.IntegerField(null=True)
    #dislikes = models.IntegerField(null=True)
    description = models.TextField(null=True)
    channel = models.TextField(null=True)
    #channel_url = models.TextField(null=True)
    #channel_subscribers = models.TextField(null=True)

    def __str__(self):
        return f'{self.videoid}:{self.title}'


class Channel(models.Model):
    channel = models.TextField(primary_key=True)
    channel_url = models.TextField(null=True)
    subscribers = models.TextField(null=True)
    views = models.TextField(null=True)
    joined = models.TextField(null=True)
    description = models.TextField(null=True)
