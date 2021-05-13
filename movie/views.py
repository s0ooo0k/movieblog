from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from movie.models import Movie

def home(request):
    movies = Movie.objects
    return render(request, 'home.html', {'movies': movies})

def detail(request, movie_id):
    movie_detail = get_object_or_404(Movie, pk= movie_id)
    return render(request, 'detail.html', {'movie': movie_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    movie = Movie()
    movie.title = request.GET['title']
    movie.body = request.GET['body']
    movie.pub_date = timezone.datetime.now()
    movie.save()

    return redirect('/movie/' + str(movie.id))

def delete(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)
    movies.delete()
    return redirect('home')