from django.shortcuts import render
from django.http import HttpResponse

def welcomeHTTP(request):
    return HttpResponse("Hello, world! This is Theia server!")
