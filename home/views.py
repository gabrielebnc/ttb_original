from django.shortcuts import render, redirect
from .models import Sneaker, SneakerImage, SneakerSize


def home_view(request):
    list_sneakers = Sneaker.objects.all()

    return render(request, 'home/home.html', {"sneakers": list_sneakers})


def redirect_to_home_view(request):
    return redirect('/home/')


def contact_us(request):
    return render(request, 'home/contact_us.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})

