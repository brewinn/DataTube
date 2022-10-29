from datatubeapp.models import Video

def initialize_database():
    Video.objects.create(videoid='000000000001', title='Cat video')
    Video.objects.create(videoid='000000000002', title='dog video')
