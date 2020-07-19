from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:puzzle_id>", views.puzzle, name="puzzle")
]