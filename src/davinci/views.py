from django.shortcuts import render
from django.http import HttpResponse

from apis.openai_api import davinci

def davinciEX(request):
    HttpResponse(davinci('What is El Quijote?'))

