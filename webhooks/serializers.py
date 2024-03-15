from rest_framework import serializers
from .models import WebhookData


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookData
        fields = (
            "id",
            "type",
            "nominalAmount",
        )
