from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from vocabulario.models import Vocabulario
from vocabulario.serializers import VocabularioSerializer
import random


def read_vocabulario_list(request):
    """
    Devuelve todas las palabras.
    """
    if request.method == 'GET':
        vocabulario = Vocabulario.objects.all()
        serializer = VocabularioSerializer(vocabulario, many=True)
        return JsonResponse(serializer.data, safe=False)

def random_palabra_view(request):
    """
    Devuelve todas las palabras
    """

    if request.method == 'GET':
        max_id = Vocabulario.objects.all().order_by("-id")[0]
        search = random.randint(1,max_id.id) # gets random id 
        palabra = Vocabulario.objects.filter(id=search)
        serializer = VocabularioSerializer(palabra, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_palabra(request):
    """
    Create new Palabra
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VocabularioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_all_by_palabra(request):
    """
    devuelve todo deacuerdo a la pabra
    """
    if request.method == 'GET':
        data = request.GET.get('palabra')
        palabra = Vocabulario.objects.filter(palabra=data)
        serializer = VocabularioSerializer(palabra, many=True)
        return JsonResponse(serializer.data, safe=False)
