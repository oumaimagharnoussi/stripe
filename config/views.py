from django.shortcuts import redirect, render
import os

import stripe
from django.conf import settings

from config.settings import STRIPE_SECRET_KEY
#stripe.api_key ='pk_test_51L6yEhIfbq4sSiOGgsDLKpYkLFcHgUWzhtHVZ0o0enFlmivyuk0A43AcjM4dVJoonLkiTevjR3LUqTHUxFOeY6fn00lQgGbaCs'





def home (request):
    return render(request, 'home.html')

stripe.api_key =  STRIPE_SECRET_KEY

def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=[
            'card',
        ],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1L7OqdIfbq4sSiOG3i0X8mjU',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000',
            cancel_url='http://localhost:8000',

    )

    return redirect(checkout_session.url, code=303)