# SKILL TEST STARK BANK

## Introduction

Project developed as part of StarkBank's technical skill test. The main goal is to issue 8 to 12 Invoices every 3 hours to random people and if the Invoice is credited, transfer the amount to a specific account. The application was developed using Python, Django, Django Rest Framework and a designated StarkBank sandbox. For webhook callbacks and API calls, webhook.site and Postman were used.

## Setup

Make sure you have the correct version of Python (3.11.5), Django and Django Rest Framework installed in your machine. The latter can be installed using the command `pip install django` / `pip install djangorestframework` directly in the command line.

As this application runs in a virtual environment, you have to update the 'pyvenv.cfg' file (which can be found inside the '.venv' folder) with your machine's information.

To activate your virtual environment, simply paste the following code to the command line:

`venv\Scripts\Activate`

After the activation, don't forget to change the environment variables. They will define the values used to identify the environment you're working with (sandbox or production), your webhook endpoint and the project/organization.
These variables are exemplified in the file `'.env.example'` in the project's core. You must change the file to `'.env'` after its update.

## Apps 

This application's functionalitites lie in three main apps: Invoices, Transfers and Webhooks, each one referencing the entities they're related to within StarkBank's environment. 

### Invoices

The logic behind the Invoice creation can be found in `invoices\views.py`. It defines a StarkBank user using environment variables and also defines the invoice quantity (8 to 12) and random people information using the random and faker libraries, respectively. 

Usually, when using Django, the functions defined in `views.py` are called from a request. As we are not dealing with requests to initiate the process, the function `create_invoice` receives no parameters. Instead, the command `python manage.py invoice_scheduling` should be used directly in the terminal to start invoice creation. This command triggers a scheduled job that calls the `create_invoice` function every 3 hours. In case you want to create a single invoice without using this scheduled job (mainly for testing), you can simply run `python manage.py new_invoices` in your terminal.

You can check out the newly created invoices accessing your StarkBank environment and clicking in "Receivables" and then "Invoices", in the left-side panel.

### Webhooks

After its creation, the next step was to establish a connection to the sandbox to receive updates about the invoice. As this application was run in a local server, it was not possible to receive the POST request with invoice updates directly. To solve this issue, a webhook endpoint provided by Webhook.site was used. The connection was established in StarkBank's environment, clicking "Integrations" and then "Webhooks", in the left panel.

At this point, it's important to run the local server to proceed with the workflow (both for webhooks and transfers). To do this, open a new terminal (separate from the one the invoice functions are running) and run the following command:

`python manage.py runserver`

 After receiving the event log in Webhook.site, the JSON was copied, pasted and sent to `webhooks\views.py` through a POST request sent by Postman. The application's endpoint (`http://127.0.0.1:8000/webhooks/webhook_view`) was defined using Django Rest Framework's APIView. The class `WebhookView` handles the incoming request and dispatches it to a `post()` handler method, which treats the JSON and if applicable, calls the `create_transfer` with the right parameter to create a new transfer.

### Transfers

If the invoice was indeed credited, `WebhookView` will call the function `create_transfer(amount)` (which can be found in `transfers\views.py`) to create a new transfer to a determined account. To accomplish this, just like the view in invoices, the function will define a StarkBank user using environment variables. It will then set the amount to the value of the parameter that was passed. In this situation, as the receiver is not going to change, the rest of the informations were hard-coded, but in a case where multiple different accounts could receive the transfer, variables could be used to define the other fields.  

You can verify if the transfer was succesfully completed accessing "Extract" in the left-side panel in StarkBank's environment.

## Additional Documentation 

For further information about StarkBank's API and SDKs, you can refer to their own documentation. Check it out:

[StarkBank API Reference](https://starkbank.com/docs/api)

[StarkBank SDKs](https://github.com/starkbank?q=sdk)









