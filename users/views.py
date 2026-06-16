from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
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
