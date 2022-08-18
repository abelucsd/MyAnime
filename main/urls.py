from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [    
    path('', views.home, name='home'),
    path('login', views.login_request, name='login_request'),
    path('register', views.registration, name='registration'),
    path('logout', views.logout_request, name='logout_request'),
]