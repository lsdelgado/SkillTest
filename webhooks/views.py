from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from transfers.views import create_transfer


class WebhookView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        event = request.data.get("event", {})
        log = event.get("log", {})
        invoice = log.get("invoice", {})

        invoice_amount = invoice.get("nominalAmount")
        log_type = log.get("type")

        if log_type == "credited":
            create_transfer(invoice_amount)

        return Response(request.data)
