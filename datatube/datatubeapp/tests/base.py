from datatubeapp.models import Video

def initialize_database():
    Video.objects.create(
        videoid='000000000001', 
        title='Cat video', 
        description='Cat standsoff with dog'
        )
    Video.objects.create(
            videoid='000000000002',
            title='dog video',
            description='Going out in the snow'
            )

def print_database():
    for video in Video.objects.all():
        print(f'{video.videoid=}')
        print(f'{video.title=}')
        print(f'{video.description=}')

