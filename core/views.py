from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def homepage(request):
    return render(request, "core/index.html")


def authorization(request):
    if request.method == 'POST':
        form = request.POST
        user_login = form["login"]
        password = form["password"]
        user = User.objects.get(username=user_login)
        if user.check_password(password):
            login(request, user)
            return redirect(homepage)

    return render(request, "core/login.html")


def signout(request):
    logout(request)
    return redirect(homepage)
