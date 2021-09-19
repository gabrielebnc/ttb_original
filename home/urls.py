from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('<sneaker_name>', views.sneaker_page, name='sneaker_page')
]
