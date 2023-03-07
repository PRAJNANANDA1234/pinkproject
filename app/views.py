from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pink(request):
    return HttpResponse('<marquee><h1>PINK IS PRETTY CLR</h1></marquee>')
