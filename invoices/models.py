from django.db import models

class Invoice(models.Model):
    amount = models.IntegerField()
    taxId = models.CharField(max_length = 60)
    name = models.CharField(max_length = 60)
    status_choices = (
        ("created", "CREATED"),
        ("sent", "SENT"),
        ("error", "ERROR"),
        ("paid", "PAID")
    )
    status = models.CharField(max_length = 7, choices = status_choices)

    def __str__(self):
        return self.name
