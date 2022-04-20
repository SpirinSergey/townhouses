from django.urls import path
from . import views
from main.decorators import check_recaptcha

urlpatterns = [
    path('', check_recaptcha(views.index), name='index'),
    path('about', check_recaptcha(views.about), name='about'),
    path('developers', check_recaptcha(views.area), name='area'),
    path('amenities', check_recaptcha(views.amenities), name='amenities'),
    path('gallery', check_recaptcha(views.gallery), name='gallery'),
    path('listings', check_recaptcha(views.available_units), name='available_units'),
    path('contacts', check_recaptcha(views.contacts), name='contacts'),
    path('privacy-policy', check_recaptcha(views.privacy), name='privacy-policy'),
    path('terms', check_recaptcha(views.terms), name='terms'),
    ]