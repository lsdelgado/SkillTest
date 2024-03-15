from django.urls import path
from . import views

urlpatterns = [
    path("create_transfer", views.create_transfer, name="create_transfer"),
]
