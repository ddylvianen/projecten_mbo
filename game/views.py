from django.shortcuts import render
from .models import *

def home(req):
    games = Game.objects.all().order_by('-date')[:6]
    calltoaction = games[0]
    return render(req, 'game/home.html', {'games': games[1:6], 'imgurl': '/media/', 'calltoaction': calltoaction})

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

def login(req):
    return render(req, "game/login.html")

def register(req):
    return render(req, "game/register.html")

def profile(req):
    return render(req, "game/profile.html")