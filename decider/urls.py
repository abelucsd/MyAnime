from django.urls import path
from . import views

app_name = 'decider'
urlpatterns = [
    path('', views.temp, name='temp'),
]