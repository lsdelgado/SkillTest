import starkbank
from StarkBank.settings import PRIVATE_KEY, STARKBANK_ENVIRONMENT, STARKBANK_PROJECT_ID


def create_transfer(amount):

    user = starkbank.Project(
        environment=STARKBANK_ENVIRONMENT,
        id=STARKBANK_PROJECT_ID,
        private_key=PRIVATE_KEY,
    )

    starkbank.user = user

    transfer = starkbank.transfer.create([
            starkbank.Transfer(
                amount=amount,
                bank_code="20018183",  
                branch_code="0001",
                account_number="6341320293482496",
                account_type="payment",
                tax_id="20.018.183/0001-80",
                name="Stark Bank S.A",
                ),     
        ])
    
    print("New transfer: ", transfer)

    return
