from django.db import models


class WebhookData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length = 100)
    nominalAmount = models.IntegerField()

    def str(self):
        return self.task
