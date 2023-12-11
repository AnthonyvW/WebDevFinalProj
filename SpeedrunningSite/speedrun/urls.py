from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("new_game", views.new_game, name="new_game"),
    path("random_game", views.random_game, name="random_game"),
    path("game/<str:title>", views.game, name="game"),
]