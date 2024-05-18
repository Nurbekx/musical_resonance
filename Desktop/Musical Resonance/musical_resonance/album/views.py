from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    albums = Album.objects.all()
    return render(request, 'album/home.html', {'albums': albums})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    reviews = album.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.album = album
            review.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = ReviewForm()
    return render(request, 'album/album_detail.html', {'album': album, 'reviews': reviews, 'form': form})


def search(request):
    query = request.GET.get('q')
    results = Album.objects.filter(title__icontains=query) | Album.objects.filter(artist__icontains=query) | Album.objects.filter(genre__icontains=query)
    return render(request, 'album/search_results.html', {'results': results})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})