from django.urls import path
from datatubeapp import views

search_urlpatterns = [
                path('query=<str:query>', views.search_page, name='search-list'),
                ]
