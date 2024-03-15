from django.core.management.base import BaseCommand
from django.utils import timezone
import schedule
import time
from invoices.views import create_invoice


class Command(BaseCommand):
    help = "Start scheduler"

    def handle(self, *args, **kwargs):

        schedule.every(3).hour.do(create_invoice)

        self.stdout.write("Waiting scheduled job", ending="")

        while True:
            schedule.run_pending()
            time.sleep(1)
