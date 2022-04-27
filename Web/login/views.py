from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def login(request):
    return HttpResponse("Hi")

def home(request):
    return render(request, 'login/about.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1>')