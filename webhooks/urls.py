from django.urls import path
from .views import (
    WebhookView,
)

urlpatterns = [
    path("webhook_view", WebhookView.as_view()),
]
