from django.urls import path
from . import views

app_name = 'favorites'
urlpatterns = [    
    path('', views.add_favorite, name='add_favorite')
]