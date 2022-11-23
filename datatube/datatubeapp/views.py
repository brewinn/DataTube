from django.shortcuts import render, redirect
from datatubeapp.forms import SearchForm

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')

    return render(request, 'base.html', {
        'form': SearchForm(),
    })


def search_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')

    modifiers = request.META['QUERY_STRING']
    return render(request, 'base.html', {
        'form': SearchForm(),
        'search_text': SearchForm.parse_query(query),
        'search_modifiers': SearchForm.parse_modifiers(modifiers),
        'search_results': SearchForm().parse_search(query, modifiers).execute_search()
    })


def channel_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')

    return render(request, 'channel.html', {
        'form': SearchForm(),
        'channel_data': SearchForm().find_channel(query)
    })
