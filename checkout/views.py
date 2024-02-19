from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from.forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OY5MYIPooaFnGz0eF3smnixjmqbOeStdoVA0ug2zLbVkbWKQBoTQmADRTNuxGLCXP4OuFYl0lB3zbzrp5PzdVDH00GTUCjDEZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)