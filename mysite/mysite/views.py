from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #   return HttpResponse("Hello, world! This is the home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world! This is the about page.")

def contact(request):
    return HttpResponse("Hello, world! This is the contact page.")
