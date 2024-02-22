from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    return render(request, 'API/index.html', context)

def map(request):
    context = {}
    return render(request, 'API/map.html', context)

def about(request):
    context = {}
    return render(request, 'API/about.html', context)

def contact(request):
    context = {}
    return render(request, 'API/contact.html', context)
