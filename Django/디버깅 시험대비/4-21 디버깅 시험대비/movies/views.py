from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    print(request.user.is_authenticated)
    context = {
        'moives' : movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie' : movie,
        'comments' : comments,
        'comment_form' : comment_form,
    }

    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')

def comment_create(request, movies_pk):
    movie = Movie.objects.get(pk = movies_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'comment_form' : comment_form,
        'movie' : movie,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)

def comment_delete(request, movies_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()

    return redirect('movies:detail', movies_pk)

def likes(request, movies_pk):

    movie = Movie.objects.get(pk=movies_pk)

    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)

    return redirect('movies:detail', movies_pk)