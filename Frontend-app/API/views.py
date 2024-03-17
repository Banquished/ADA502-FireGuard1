from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response

# Create your views here.

# Dummy Example on how to use APIView
class ReactView(APIView):
    def get(self, request):
        output = [{"employee": output.employee, "department": output.department} for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


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
