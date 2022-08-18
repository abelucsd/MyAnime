from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login 
from django.contrib import messages

def home(request):
    return render(request, "main/home.html")

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main/home.html")            
        messages.error(request, "Unsuccessful registration.")
    form = RegistrationForm()
    return render(request, "main/registration.html", {"registration_form": form})