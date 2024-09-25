from django.urls import include, path

from . import views

app_name = "projects"
urlpatterns = [
    path("", views.index, name="index"),
]