from django.shortcuts import render, redirect
from datatubeapp.forms import SearchForm

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')
    
    return render(request, 'home.html', {
        'form': SearchForm(),
        'search_results': None
        })

def search_page(request, query):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        return redirect(f'/search/{form.url()}')
    
    modifiers = request.META['QUERY_STRING']
    return render(request, 'search.html', {
        'form': SearchForm(),
        'search_text': query,
        'search_results': SearchForm().parse_search(query, modifiers).execute_search()
        })
    
