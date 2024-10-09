from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("input/", views.input_view, name='input_view')
]