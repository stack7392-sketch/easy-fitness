from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def auth_page(request):
    if request.method == "POST":
        action = request.POST.get("action")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if action == "register":
            if User.objects.filter(username=username).exists():
                return render(request, "accounts/auth.html", {
                    "register_error": "Username already exists"
                })

            User.objects.create_user(username=username, password=password)
            return redirect("/")

        if action == "login":
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/dashboard/")
            else:
                return render(request, "accounts/auth.html", {
                    "login_error": "Invalid username or password"
                })

    return render(request, "accounts/auth.html")


def user_logout(request):
    logout(request)
    return redirect("/")


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html", {
        "username": request.user.username
    })


@login_required
def settings_page(request):
    return render(request, "accounts/settings.html")
