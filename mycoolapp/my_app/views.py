from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello my cool app>')
