from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html")


def student_list(request):
    students = Student.objects.all()

    return render(request, "home/student_list.html", {"students": students})
