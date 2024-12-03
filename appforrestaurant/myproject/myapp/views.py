from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
from django.shortcuts import render

# Create your views here.
