from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('stylists/', views.stylists, name='stylists'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('location/', views.location, name='location'),
    path('book/', views.book_appointment, name='book'),
    path('about/', views.about, name='about'),
]
