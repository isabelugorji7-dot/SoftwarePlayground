from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def breakfast(request):
    return render(request, 'breakfast.html')

def lunch(request):
    return render(request, 'lunch.html')

def dinner(request):
    return render(request, 'dinner.html')

def kids(request):
    return render(request, 'kids.html')

def drinks(request):
    return render(request, 'drinks.html')

def contact(request):
    return render(request, 'contact.html')

def reservations(request):
    return render(request, 'reservations.html')

def locateus(request):
    return render(request, 'locateus.html')

# Seasonal menus
def summer(request):
    return render(request, 'menus/seasons/summer.html')

def autumn(request):
    return render(request, 'menus/seasons/autumn.html')

def winter(request):
    return render(request, 'menus/seasons/winter.html')

def spring(request):
    return render(request, 'menus/seasons/spring.html')
