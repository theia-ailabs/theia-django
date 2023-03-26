from django.shortcuts import render
from django.http import Response
from services.apis.openai_api import davinci


@api_view(['GET'])
def theia(request):
    response = {}
    solute = request.GET.get('solute')
    solvent = request.GET.get('solvent')
    results = [solute, solvent]
    return Response({'result': results}, status=200)
