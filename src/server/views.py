# Server views.py
import asyncio
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from services.whispher_ai import localWhispher


def welcome(request):
    return HttpResponse("Hello, world! This is Theia Brain!")


async def theia(request):

    if request.method == 'POST':
        question = request.POST.get('my_string')
        answer = await localWhispher(question)
        response = {
            'status': 200,  # Success response
            'answer': answer,
            'text': answer
        }
        # Ask to davinci
        return JsonResponse(response)
    else:
        response_error = {
            'status': 404
            'error': 'Invalid request method',

        }
        return JsonResponse(response_error, status=400)
