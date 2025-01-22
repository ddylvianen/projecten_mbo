from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("game_list/", views.game_list, name="game_list"),
    path("faq/", views.faq, name="faq"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("game/<int:id>/", views.game, name="game"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
]