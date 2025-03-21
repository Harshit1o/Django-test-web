from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! this will be deployed to kubernetes, and whole process is automated!!!!!")
