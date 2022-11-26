from .base import initialize_database
from django.test import TestCase
from datatubeapp.models import Video

# Create your tests here.


class VideoModelsTest(TestCase):
    '''Tests for the video table'''

    def test_empty_video(self):
        video = Video()
        self.assertIsNotNone(video.videoid)

    def test_videoid_length(self):
        initialize_database()
        video = Video.objects.first()
        max_length = video._meta.get_field('videoid').max_length
        self.assertEqual(max_length, 12)

    def test_video_name_is_id_and_title(self):
        initialize_database()
        video = Video.objects.first()
        expected_video_name = f'{video.videoid}:{video.title}'
        self.assertEqual(str(video), expected_video_name)
