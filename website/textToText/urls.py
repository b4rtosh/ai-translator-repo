from django.urls import path
from . import views

urlpatterns = [
    path("", views.text_to_text_view, name='text_to_text_view'),
]