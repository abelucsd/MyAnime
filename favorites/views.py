from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Anime, Genre
from .forms import AnimeForm
from django.contrib import messages

# Create your views here.

def add_favorite(request):
    """
        Adds user input to favorite anime list.        
    """
    
    if request.method == 'Post':
        form = AnimeForm(request, data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            genre = form.cleaned_data.get('genre')
            personal_rating = form.cleaned_data.get('personal_rating')

            # need to add User
            # could do a save and then query user then edit the 
            # anime model or directly edit the user data in form
            if title is not None:
                # do another messages later
                messages.info(request, f"You have added {title}.")
                return redirect('favorites:add_favorite')
            else:
                messages.error(request, 'Please insert title.')
        else:
            messages.error(request, 'Invalid input.')
    form = AnimeForm()
    return render(request, 'favorites/favorite.html', {'add_favorite_form': form})