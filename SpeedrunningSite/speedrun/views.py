from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import User, Profile

def index(request):
    return render(request, "index.html")

def contact_us(request):
    return render(request, "contact_us.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next", "index")
            return redirect(next_url)
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        next_url = request.GET.get("next", "index")
        return render(request, "login.html", {"next": next_url })

def logout_view(request):
    logout(request)
    return redirect("index")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        if username == "":
            return render(request, "register.html", {
                "message": "Please enter a username."
            })
        
        if email == "":
            return render(request, "register.html", {
                "message": "Please enter a valid email."
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password == "":
            return render(request, "register.html", {
                "message": "Please enter a password."
            })

        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "register.html")

def profile(request, username):
    user = User.objects.get(username=username)

    profile = Profile.objects.get(user=user)

    name = user.username
    pfp = profile.profile_picture

    return render(request, "user_profile.html", {
        "name": name,
        "pfp": pfp
    })
