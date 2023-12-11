from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import User
from .forms import GameForm, SpeedrunForm

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

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
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

def new_game(request):
    if request.method == "POST":
        if "cancel" in request.POST: 
            return redirect('index')
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.creator = request.user
            game.save()
            form.save_m2m()
            messages.success(request, f'Game created successfully!')
            return redirect("index")
        else:
            messages.error(request, 'Problem creating the game. Details below.')	
    else: 
        form = GameForm()
    return render(request, "new_game.html", {'form':form})
