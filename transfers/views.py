import starkbank


private_key_content = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIDFJtcnGx+Ff1UZ25MCtLJVEoKn2m0OIJj9UQBUGYqL2oAcGBSuBBAAK
oUQDQgAE9aVOC9xjxK1AIMFO8obvEis4qSOJMo+dYszHP/E9Ie13xDKfj8OowiQv
gpKyInwOwi/rYI+1NiqTF1fB19P1yA==
-----END EC PRIVATE KEY-----
"""

user = starkbank.Project(
    environment="sandbox", id="6274920858255360", private_key=private_key_content
)

starkbank.user = user

def create_transfer(amount):

    transfers = starkbank.transfer.create([
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

    for transfer in transfers:
        print(transfer)

    print("CHEGOU NA TRANSFERS VIEWS")

    return
