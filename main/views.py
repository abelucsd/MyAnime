from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request, "main/home.html")
    else:
        # should go to login
        return redirect("main:login_request")        

def login_request(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)        
        if form.is_valid():            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:            
            messages.error(request, "Invalid username or password.")
    form = CustomAuthenticationForm()
    return render(request, 'main/login.html', {'login_form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:home")

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:home")            
        messages.error(request, "Unsuccessful registration.")
    form = RegistrationForm()
    return render(request, "main/registration.html", {"registration_form": form})

