from binascii import rledecode_hqx
from django.db import connection
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .forms import commentForms

from .models import *


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
    if request.method == 'POST':
        form = commentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_single')
        else:
           error = "Incorrect form"

    com = comment.objects.order_by('author')
    form = commentForms()

    data = {
        'form': form
    }
    return render(request, 'login/blog-single.html', {'com':com})

def contact(request):
    return render(request, 'login/contact.html')
    
def index(request):
    return render(request, 'login/index.html')

def account(request):
    return render(request, 'login/account.html')
    

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1>')
