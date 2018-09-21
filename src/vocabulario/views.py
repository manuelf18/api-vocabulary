from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets,status,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from vocabulario.models import Vocabulario
from vocabulario.serializers import VocabularioSerializer

import random

class VocabularioViewSet(viewsets.ModelViewSet):
    queryset = Vocabulario.objects.all()
    serializer_class = VocabularioSerializer

    @action(methods=['get', ], url_path='palabra_del_dia', url_name='palabra_del_dia', detail=False)
    def random_word(self, request):
        qs = self.queryset.values_list('id', flat=True)
        word_id = random.choice(qs)
        serializer = self.get_serializer(Vocabulario.objects.get(id=word_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

class VocabularioList(generics.ListAPIView):
    serializer_class = VocabularioSerializer
    queryset = Vocabulario.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        palabra = self.request.query_params.get('palabra', None)
        if not palabra:
            return self.queryset.none()
        return self.queryset.filter(palabra__icontains=palabra)

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
