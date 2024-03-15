from django.core.management.base import BaseCommand
from django.utils import timezone
import schedule
import time
from invoices.views import create_invoice


class Command(BaseCommand):
    help = "Create invoices"

    def handle(self, *args, **kwargs):

        create_invoice()


