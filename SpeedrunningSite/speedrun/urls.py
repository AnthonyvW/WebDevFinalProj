from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #path("login/", views.login_view, name="login"),
    #path("logout/", views.logout_view, name="logout"),
    #path("register/", views.register_view, name="register"),

    path("", views.index, name="index"),
]