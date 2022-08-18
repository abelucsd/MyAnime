from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add_favorite(request):
    """
        Adds user input to favorite anime list.        
    """
    return render(request, 'favorites/favorite.html')