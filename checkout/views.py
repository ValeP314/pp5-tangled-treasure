from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('items'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NYowhKBsjoXtXIip5JAxylf3r94XQ8iWOk3P3vNCczWwH2exZGFmS2VomgUVJDqxQqHeQRAMbQYTuP6sJwziw4c00sUh87LBH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
