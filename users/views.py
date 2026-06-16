from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created successfully for {username}!")
            return redirect("users:users_list")
    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("students:students_list")
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", {"form": form})
