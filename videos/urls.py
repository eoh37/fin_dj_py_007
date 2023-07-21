from django.urls import path

from . import views

app_name = "videos"
urlpatterns = [
    path("", views.index, name="index"),
    path("videos/<int:quantity>/", views.videos, name="videos"),
]
