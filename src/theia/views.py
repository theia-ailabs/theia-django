from django.shortcuts import render
from django.http import HttpResponse
from services.apis.openai_api import davinci


def theia(request):
    HttpResponse(davinci('What is El Quijote?'))
