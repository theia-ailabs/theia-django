from django.shortcuts import render
from django.http import HttpResponse
from services.apis.openai_api import davinci
from django.dispatch import receiver


# def theia(request):
#     return HttpResponse(davinci('What is El Quijote?'))

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# @receiver(post_save, sender=senderMyModel)
# def theia(sender, instance, *args, **kwargs):
#     channel_layer = get_channel_layer()
#     group_name = "my group"
#     async_to_sync(channel_layer.group_send)(
#         group_name,
#         {
#             'type': 'notification.message',
#             'data': {"hello": 1}
#         }
#     )


# views.py
import asyncio

from django.http import JsonResponse


async def theia(request):
    # Retrieve the input string from the request
    input_string = request.GET.get('input_string')

    # Do some asynchronous processing
    await asyncio.sleep(5)  # simulate some long-running task

    # Prepare the response
    output_string = f"You entered: {input_string} (processed asynchronously)"
    response = {'output_string': output_string}

    # Return the response as JSON
    return JsonResponse(response)


def welcome(request):
    return HttpResponse("Hello, world! This is Theia Brain!")
