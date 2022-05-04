from django.db import connection
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def sing_in(request):
    return render(request, 'login/sing_in.html')

def log_in(request):
    return render(request, 'login/log_in.html')

def home(request):
    return render(request, 'login/about.html')

def packages(request):
    return render(request, 'login/packages.html')

def blog_home(request):
    return render(request, 'login/blog-home.html')

def hotels(request):
    return render(request, 'login/hotels.html')

def insurance(request):
    return render(request, 'login/insurance.html')

def blog_single(request):
    return render(request, 'login/blog-single.html')

def contact(request):
    return render(request, 'login/contact.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1>')
