from django.shortcuts import render, redirect


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
