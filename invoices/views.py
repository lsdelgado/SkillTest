import starkbank
from faker import Faker
import random
from StarkBank.settings import PRIVATE_KEY, STARKBANK_ENVIRONMENT, STARKBANK_PROJECT_ID


def create_invoice():

    user = starkbank.Project(
        environment=STARKBANK_ENVIRONMENT, 
        id=STARKBANK_PROJECT_ID, 
        private_key=PRIVATE_KEY
    )

    starkbank.user = user

    invoice_quantity = random.randint(8, 12)
    fake = Faker("pt_BR")
    
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
