from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def stylists(request):
    return render(request, 'stylists.html')

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    return render(request, 'reviews.html')

def faq(request):
    return render(request, 'FAQ.html')

def contact(request):
    return render(request, 'contact.html')

def location(request):
    return render(request, 'location.html')

def book_appointment(request):
    return render(request, 'book_appointment.html')

def about(request):
    return render(request, 'about.html')
