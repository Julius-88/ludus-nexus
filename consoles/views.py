from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


def playstation(request):
    """ A view to return the playstation page """
    products = Product.objects.filter(console__name='Playstation')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'playstation',
    }
    return render(request, 'consoles/playstation.html', context)


def xbox(request):
    """ A view to return the xbox page """
    products = Product.objects.filter(console__name='Xbox')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'xbox',
    }
    return render(request, 'consoles/xbox.html', context)


def nintendo(request):
    """ A view to return the nintendo page """
    products = Product.objects.filter(console__name='Nintendo')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'nintendo',
    }
    return render(request, 'consoles/nintendo.html', context)


# View for Admin to add products
@login_required
@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'consoles/add_product.html', {'form': form})


# View for Admin to delete products
@login_required
@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('home')

    return render(
        request,
        'consoles/delete_product.html',
        {'product': product})


# View for Admin to edit_products
@login_required
@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('home')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'consoles/edit_product.html',
        {'form': form})
