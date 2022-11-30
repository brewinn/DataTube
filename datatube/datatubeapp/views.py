from django.shortcuts import render, redirect
from datatubeapp.forms import SearchForm
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if 'react' in request.POST:
            return redirect(f'/search/r/{form.r_url()}')
        return redirect(f'/search/{form.url()}')

    return render(request, 'base.html', {
        'form': SearchForm().as_ul(),
    })


def search_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')

    modifiers = request.META['QUERY_STRING']

    return render(request, 'base.html', {
        'form': SearchForm().as_ul(),
        'search_text': SearchForm.parse_query(query),
        'search_modifiers': SearchForm.parse_modifiers(modifiers),
        'search_results': SearchForm().parse_search(query, modifiers).execute_search()
    })


def channel_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')
    if query[-3:] == 'r45':
        result = SearchForm().find_channel(query[:-3])
        result2 = SearchForm().find_channel_videos(query[:-3])
        data = serializers.serialize('json', list(chain(result, result2)))
        return HttpResponse(data, content_type='application/json')

    return render(request, 'channel.html', {
        'form': SearchForm().as_ul,
        'channel_data': SearchForm().find_channel(query),
        'channel_video_results': SearchForm().find_channel_videos(query),
    })

def video_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')

    return render(request, 'video.html', {
        'form': SearchForm().as_ul(),
        'video_result': SearchForm().find_video(query),
        'video_tags': SearchForm().find_video_tags(query),
    })

    
def react_search(request,query):
    query = query.replace('%3D','=')
    query = query.replace('%26','&')
    parts = query.split('--')
    result = SearchForm().parse_search(parts[0], parts[1]).execute_search()
    data = serializers.serialize('json', result)
    return HttpResponse(data, content_type='application/json')

