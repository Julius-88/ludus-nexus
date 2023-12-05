from django.shortcuts import render, redirect
from .models import Order, OrderDetail, Product
from django.contrib.auth.decorators import login_required


def view_bag(request):
    """ A view to return the cart contents page """
    return render(request, 'bag/bag.html')


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


@login_required
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        city = request.POST.get('city')

        # Create Order instance
        order = Order.objects.create(
            user=request.user,
            address=address,
            postcode=postcode,
            city=city,
        )

        # Retrieve cart from session
        cart = request.session.get('bag', {})

        # Create OrderDetail for each item in the cart
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderDetail.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                orderdetail_total=product.price * quantity
            )

        # Update the order total
        order.update_total()

        # Clear the cart from session
        request.session['bag'] = {}

        # Redirect to order confirmation page with order's id
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'bag/checkout.html')


def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {
        'order': order
        }
    return render(request, 'bag/order_confirmation.html', context)


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'bag/user_orders.html', {'orders': orders})
