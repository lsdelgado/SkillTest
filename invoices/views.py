from django.http import HttpResponse
import starkbank
from faker import Faker
import random
import schedule
import time
from StarkBank.settings import PRIVATE_KEY


def create_invoice():

    print(PRIVATE_KEY)

    user = starkbank.Project(
        environment="sandbox", 
        id="6274920858255360", 
        private_key=PRIVATE_KEY
    )

    starkbank.user = user

    invoice_quantity = random.randint(8, 12)
    fake = Faker("pt_BR")
    print(invoice_quantity)

    invoices = []

    for i in range(invoice_quantity):

        invoice = starkbank.invoice.create(
            [
                starkbank.Invoice(
                    amount=fake.random_int(min=0, max=999999),
                    name=fake.name(),
                    tax_id=fake.cpf(),
                )
            ]
        )

        invoices.append(invoice)
    print("Created invoices: ", invoices)

    return


#create_invoice()




























'''def create_invoice(request):

    invoice_number = random.randint(8, 12)
    fake = Faker("pt_BR")

    if request.method == 'GET':
        for i in range (invoice_number):
            name = fake.name()
            amount = fake.random_int(min=0, max=9999)
            taxId = fake.cpf()

            invoice = Invoice(name = name, 
                              amount = amount, 
                              taxId = taxId, 
                              status = "created",)
            invoice.save()



    return '''
