from django.shortcuts import render
from .models import Gallery, Listing
from django.db.models import Q


def index(request):
    return render(request, 'main/pages/index.html')


def about(request):
    return render(request, 'main/pages/about.html')


def area(request):
    return render(request, 'main/pages/area.html')


def amenities(request):
    return render(request, 'main/pages/amenities.html')


def gallery(request):
    gal_img = Gallery.objects.all()
    return render(request, 'main/pages/gallery.html', context={'gal_img': gal_img})


def available_units(request):
    return render(request, 'main/pages/available_units.html')


def contacts(request):
    return render(request, 'main/pages/contacts.html')


def privacy(request):
    return render(request, 'main/pages/privacy-policy.html')


def terms(request):
    return render(request, 'main/pages/terms.html')
