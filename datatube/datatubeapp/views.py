from django.shortcuts import render, redirect
#from django.views.generic.list import ListView
#from django.utils import timezone
from datatubeapp.forms import SearchForm
#from datatubeapp.models import Video

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
    
    return render(request, 'search.html', {
        'form': SearchForm(),
        'search_results': SearchForm().parse_query(query).execute_search()
        })
    
'''
class SearchListView(ListView):

    model = Video
    paginate_by = 35
    context_object_name = 'search_results'
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self, *args, **kwargs):
        query = self.request.POST.get('query')
        return Video.objects.filter(title__contains=query)
'''
