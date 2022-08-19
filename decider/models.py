from django.db import models

# Create your models here.
'''
class Mood(models.Model):
    genres = models.ManyToManyField(Genre)
    MOOD_CHOICES = [
        ('adventurous', 'Adventurous'), ('discontent', 'Discontent'), ('lonely', 'Lonely'),
        ('romantic', 'Romantic'), ('heartbroken', 'Heartbroken'), ('optimistic', 'Optimistic'),
        ('sad', 'Sad'), ('stressed', 'Stressed')
    ]
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
'''