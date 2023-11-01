from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Comentario
from .forms import CommentsForm
from django.contrib.auth.decorators import (login_required, permission_required)

# Create your views here.
def index(request):

    movies = Movie.objects.all()

    return render(request, 'home.html', {'movies':movies})

def get_movie(request, id):
    movie = Movie.objects.get(id=id)

    comentarios = Comentario.objects.filter(movie=id)

    form = CommentsForm()

    return render(request, 'moviesingle.html',
                  {'movie':movie,
                   'comentarios': comentarios,
                   'form': form})

@login_required
@permission_required('movie.add_comentario', raise_exception=True)
def add_new_comment(request, id):
    if request.method == 'POST':
        form = CommentsForm(request.POST)

        if form.is_valid():
            user = request.user
            movie = Movie.objects.get(id=id)

            new_comment = form.save(commit=False)
            new_comment.usuario = user
            new_comment.movie = movie

            new_comment.save()
        return redirect('get_movie', id)
    
    else:
        return redirect('get_movie', id)


