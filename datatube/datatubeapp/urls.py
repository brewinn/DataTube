from django.urls import path
from datatubeapp import views

search_urlpatterns = [
    path('query=<str:query>/modifiers', views.search_page, name='search-list'),
    path('query=<str:query>', views.search_page, name='search-list'),
]

channel_urlpatterns = [
    path('<str:query>', views.channel_page, name='channel-view'),
]

video_urlpatterns = [
    path('<str:query>', views.video_page, name='video-view'),
]
