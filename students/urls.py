from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.student_list, name="students_list"),
    path("students/add/", views.student_create, name="students_create"),
    path("students/<int:id>/edit", views.student_edit, name="students_edit"),
    path("students/<int:id>/delete", views.student_delete, name="students_delete"),
]
