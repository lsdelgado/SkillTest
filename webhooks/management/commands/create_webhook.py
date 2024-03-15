from django.core.management.base import BaseCommand
import starkbank
from StarkBank.settings import WEBHOOK_URL


class Command(BaseCommand):
    help = "Create webhook"

    def handle(self, *args, **kwargs):

        starkbank.webhook.create(
            url=WEBHOOK_URL,
            subscriptions=["invoice"],
        )

        self.stdout.write("Created webhook", ending="")
