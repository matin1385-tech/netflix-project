from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='netflix/images/', blank=True, null=True)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    trailer_url = models.URLField(blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, blank=True, related_name="movies")
    directors = models.ManyToManyField(Director, blank=True, related_name="movies")

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="in_watchlists")

    def __str__(self):
        return f"{self.user.username} → {self.movie.title}"
