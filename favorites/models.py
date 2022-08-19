from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FavoriteAnimes(models.Model):
    """
        User's Favorite Anime
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Anime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    personal_rating = models.IntegerField(default=5)

class Genre(models.Model):
    anime = models.ForeignKey(Anime, related_name='genre', on_delete=models.CASCADE)
    ACTION = 'ACTION'
    ADVENTURE = 'ADVENTURE'
    COMEDY = 'COMEDY'
    DRAMA = 'DRAMA'
    FANTASY = 'FANTASY'
    GOURMET = 'GOURMET'
    MYSTERY = 'MYSTERY'
    ROMANCE = 'ROMANCE'
    SCIFI = 'SCIFI'
    SLICE_OF_LIFE = 'SLICE_OF_LIFE'
    SPORTS = 'SPORTS'
    GENRE_CHOICES = [
        (ACTION, 'Action'), (ADVENTURE, 'Adventure'), (COMEDY, 'Comedy'), (DRAMA, 'Drama'), 
        (FANTASY, 'Fantasy'), (GOURMET, 'Gourmet'), (MYSTERY, 'Mystery'), (ROMANCE, 'Romance'), 
        (SCIFI, 'Sci-Fi'), (SLICE_OF_LIFE, 'Slice of Life'), (SPORTS, 'Sports')
    ]

    # choiceField?
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default=DRAMA)