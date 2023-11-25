from django.shortcuts import render

# Create your views here.


def playstation(request):
    """ A view to return the playstation page """
    return render(request, 'consoles/playstation.html')


def xbox(request):
    """ A view to return the xbox page """
    return render(request, 'consoles/xbox.html')


def nintendo(request):
    """ A view to return the nintendo page """
    return render(request, 'consoles/nintendo.html')
