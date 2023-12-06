from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderDetail, Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def view_bag(request):
    """ A view to return the cart contents page """
    return render(request, 'bag/bag.html')


def success(request, order_id):
    """ A view to return the success page with order details """
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'bag/success.html', {'order': order})


def payment(request, order_id):
    """ A view to return the payment page """
    order = get_object_or_404(Order, id=order_id)

    # Calculate total for Stripe
    stripe_total = int(order.total_price * 100)

    # Create a Stripe PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency='eur'
    )

    context = {
        'order_id': order_id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret
    }
    return render(request, 'bag/payment.html', context)


def process_payment(request, order_id):
    """ Process the Stripe payment """
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        try:
            # Confirm the PaymentIntent
            token = request.POST.get('stripeToken')

            stripe.Charge.create(
                amount=int(order.total_price * 100),  # Convert amount to cents
                currency='eur',
                description='Your purchase description',
                source=token
            )

            # Update order payment status to 'Paid'
            order.payment_status = 'Paid'
            order.save()

            # Redirect to the success page
            return redirect('success', order_id=order.id)
        except stripe.error.CardError as e:
            # Handle Stripe Card Error
            context = {
                'order_id': order_id,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                'error_message': e.user_message,
            }
            return render(request, 'bag/payment.html', context)

    return redirect('success', order_id=order.id)


def add_to_bag(request, product_id):
    """ Add a quantity of specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, product_id):
    """ Remove a quantity of specified product from the shopping bag """

    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if product_id in bag:
        # Decrease the quantity or remove the product if quantity becomes zero
        quantity = int(request.POST.get('quantity', 1))
        if bag[product_id] > quantity:
            bag[product_id] -= quantity
        else:
            del bag[product_id]

    request.session['bag'] = bag
    return redirect(redirect_url)


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        city = request.POST.get('city')

        # Create Order instance
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            address=address,
            postcode=postcode,
            city=city,
            payment_status='Pending',
            total_price=0,
            payment_method='Stripe'
        )

        # Retrieve cart from session
        cart = request.session.get('bag', {})

        # Create OrderDetail for each item in the cart and update total_price
        total_price = 0
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            subtotal = product.price * quantity
            order_detail = OrderDetail.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                orderdetail_total=subtotal
            )
            total_price += order_detail.orderdetail_total

        # Update the order total
        order.total_price = total_price
        order.save()

        # Clear the cart from session
        request.session['bag'] = {}

        # Redirect to payment page with the order ID
        return redirect('payment', order_id=order.id)
    else:
        return render(request, 'bag/checkout.html')


def order_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'bag/order_receipt.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'bag/order_history.html', {'orders': orders})
