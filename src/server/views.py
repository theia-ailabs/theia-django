from django.shortcuts import render
from django.http import HttpResponse
from services.apis.openai_api import davinci


def theia(request):
    return HttpResponse(davinci('What is El Quijote?'))


def welcome(request):
    return HttpResponse("Hello, world! This is Theia server!")
