from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("game_list/", views.game_list, name="game_list"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
    path("game/<int:id>/", views.game, name="game"),
]