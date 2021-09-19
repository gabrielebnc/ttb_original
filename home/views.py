from django.shortcuts import render, redirect, get_object_or_404
from .models import Sneaker, SneakerImage, SneakerSize
from django.http import HttpResponse

def home_view(request):
    list_sneakers = Sneaker.objects.all()

    return render(request, 'home/home.html', {"sneakers": list_sneakers})


def redirect_to_home_view(request):
    return redirect('/home/')


def contact_us(request):
    return render(request, 'home/contact_us.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def sneaker_page(request, sneaker_name):
    sneaker = get_object_or_404(Sneaker, name=sneaker_name)
    return render(request, 'home/sneaker_page.html', {"sneaker": sneaker})