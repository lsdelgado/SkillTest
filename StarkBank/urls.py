from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("invoices/", include("invoices.urls")),
    path("webhooks/", include("webhooks.urls")),
    path("transfers/", include("transfers.urls")),
]
