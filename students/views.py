from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def student_list(request):
    students = Student.objects.all()

    return render(request, "home/student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("students:students_list")
    else:
        form = StudentForm()
    return render(
        request,
        "home/students_create.html",
        {
            "form": form,
        },
    )


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        studentSingleForm = StudentForm(request.POST, instance=student)

        if studentSingleForm.is_valid():
            studentSingleForm.save()
            return redirect("students:students_list")

    else:
        studentSingleForm = StudentForm(instance=student)
    return render(
        request,
        "home/student_edit.html",
        {
            "studentSingleForm": studentSingleForm,
        },
    )
