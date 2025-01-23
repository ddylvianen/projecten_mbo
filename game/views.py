from datetime import datetime
from django.shortcuts import render#, get_object_or_404
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib import messages

@login_required(login_url='/login')
def home(req):
    games = Game.objects.all().order_by('-date')[:6]
    calltoaction = games[0]
    return render(req, 'game/home.html', {'games': games[1:6], 'imgurl': '/media/', 'calltoaction': calltoaction})

@login_required(login_url='/login')
def game_list(req):
    games = Game.objects.all().order_by('-date')
    return render(req, "game/gamelist.html", {'games': games, 'imgurl': '/media/'})

def faq(req):
    return render(req, "game/faq.html")

def aboutus(req):
    return render(req, "game/aboutus.html")


def game(req, id):
    game = Game.objects.get(id=id)
    reviews = Review.objects.filter(game=game)
    return render(req, "game/gameinfo.html", {'game': game, 'reviews': reviews, 'imgurl': '/media/'})

def login_user(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.success(req, 'Logged in successfully!');
                return redirect('home')  # redirect to a custom URL or view
    else:
        form = LoginForm()

    return render(req, 'game/login.html', {'form': form})

def register(req):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "game/register.html"

    if req.method == "POST":
        form = form_class(req.POST)
        if form.is_valid():
            form.save()
            # login(req, authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
            messages.success(req, 'Account created successfully');
            # return redirect(success_url)
            return redirect('login')
    else:    
        form = form_class()
    return render(req, template_name, {'form': form})

def logout_user(req):
    logout(req)
    messages.success(req, 'Logged out successfully!');
    return redirect('home')

 
