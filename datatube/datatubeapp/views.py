from django.shortcuts import render, redirect
from datatubeapp.forms import SearchForm

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
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

    return render(request, 'channel.html', {
        'form': SearchForm().as_ul(),
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
