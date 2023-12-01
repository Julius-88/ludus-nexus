from django.shortcuts import render
from .models import Product
from django.conf import settings

# Create your views here.


def playstation(request):
    """ A view to return the playstation page """
    products = Product.objects.filter(console__name='Playstation')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'playstation'
    }
    return render(request, 'consoles/playstation.html', context)


def xbox(request):
    """ A view to return the xbox page """
    products = Product.objects.filter(console__name='Xbox')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'xbox'
    }
    return render(request, 'consoles/xbox.html', context)


def nintendo(request):
    """ A view to return the nintendo page """
    products = Product.objects.filter(console__name='Nintendo')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'console_type': 'nintendo'
    }
    return render(request, 'consoles/nintendo.html', context)


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'includes/searchbar.html', context)
