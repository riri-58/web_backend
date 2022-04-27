from django.http import HttpResponse
from django.shortcuts import render

def db(request):
    return HttpResponse("db table")
