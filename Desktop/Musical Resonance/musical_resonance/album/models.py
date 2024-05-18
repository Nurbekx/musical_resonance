from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/')

    def __str__(self):
        return f'{self.title} от исполнителя: {self.artist}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.user.username} для {self.album.title}'
