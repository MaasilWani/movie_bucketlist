from django.shortcuts import render
from movieApp.models import Movie
from movieApp.forms import MovieForm

# Create your views here.

def homepage_view(request):
    return render(request, 'homepage.html')

def form_view(request):
    mydic = {}
    if request.method == 'GET':
        form = MovieForm()
        mydic = {'form':form}
        return render(request, 'form.html', context=mydic)
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return homepage_view(request)
        else:
            mydic = {'form': form}
            return render(request, 'form.html', context=mydic)

def table_view(request):
    list = Movie.objects.all()
    mydic = {'list':list}
    return render(request, 'table.html', context=mydic)