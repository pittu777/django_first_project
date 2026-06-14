from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("students/", views.student_list, name="students_list"),
]
