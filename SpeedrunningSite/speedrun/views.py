from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

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
            return render(request, "speedrun/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        next_url = request.GET.get("next", "index")
        return render(request, "speedrun/login.html", {"next": next_url })

def logout_view(request):
    pass

def register_view(request):
    pass