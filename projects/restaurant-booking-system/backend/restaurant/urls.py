"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookings.views import (
    home, menu, breakfast, lunch, dinner, kids, drinks, gallery,
    contact, reservations, locateus,
    summer, autumn, winter, spring
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('breakfast/', breakfast, name='breakfast'),
    path('lunch/', lunch, name='lunch'),
    path('dinner/', dinner, name='dinner'),
    path('kids/', kids, name='kids'),
    path('drinks/', drinks, name='drinks'),
    path('contact/', contact, name='contact'),
    path('reservations/', reservations, name='reservations'),
    path('locateus/', locateus, name='locateus'),
    path('gallery/', gallery, name='gallery'),

    # Seasonal menus
    path('summer/', summer, name='summer'),
    path('autumn/', autumn, name='autumn'),
    path('winter/', winter, name='winter'),
    path('spring/', spring, name='spring'),
]
