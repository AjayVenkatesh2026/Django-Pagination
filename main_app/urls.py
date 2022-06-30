from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("student/<int:id>", views.student, name="student"),
    path("student/edit/<int:id>", views.edit, name="edit"),
    path("student/create", views.create, name="create"),
    path("student/delete/<int:id>", views.delete, name="delete"),
]
