from secrets import choice
from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from .models import Anime, Genre
from django.forms.widgets import Select

'''
MOOD_CHOICES = [
    ('adventurous', 'Adventurous'), ('discontent', 'Discontent'), ('lonely', 'Lonely'),
    ('romantic', 'Romantic'), ('heartbroken', 'Heartbroken'), ('optimistic', 'Optimistic'),
    ('sad', 'Sad'), ('stressed', 'Stressed')
    ]
RATING_CHOICES = []

# Create a dictionary which maps genre to mood
GENRE_TO_MOOD = {
    'ACTION': ['optimistic'],
    'ADVENTURE': ['adventurous', 'optimistic'],
    'COMEDY': ['heartbroken', 'lonely', 'sad', 'stressed'],
    'DRAMA': ['content', 'romantic'],
    'FANTASY': ['adventurous'],
    'GOURMET': ['adventurous'],
    'MYSTERY': ['adventurous'],
    'ROMANCE': ['romantic'],
    'SCIFI': ['content'],
    'SLICE_OF_LIFE': ['discontent', 'stressed', 'stressed'],
    'SPORTS': ['discontent']
}
'''

class GenreSelectorWidget(Select):
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
    def __init__(self, attrs=None, choices=GENRE_CHOICES):
        super().__init__(attrs=attrs, choices=choices)        
        
    '''
    def decompress(self, value):
        if value:
            return [value.GENRE_CHOICES]
        return [None]
    '''


class AnimeForm(ModelForm):    
    
    class Meta:
        model = Anime
        fields = ['title', 'personal_rating']
        widgets = {
            'title': Textarea(attrs={
                'required': True,
                'placeholder': 'Title',
                'size': 100,                
            }),
            #genre': forms.Select(attrs={'placeholder': 'Genre'})
            #GenreSelectorWidget(widgets={choice: choice, 'placeholder': 'Genre'})
        }

# select Genre then associate it to the Anime
