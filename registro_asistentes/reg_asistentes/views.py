from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AsistenteSerializador
from .serializer import FechaInputSerializador
from .models import Asistente


"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Listar todos by nombre' : '/asis-list/',
        'Listar rango de fecha' : '/asis-list-date/',
        'Agregar' : '/asis-create/',
        'Obtener Detalles' : '/asis-detail/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def asisList(request):
    asist = Asistente.objects.all().order_by('nombres')
    serializer = AsistenteSerializador(asist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def asisDetail(request, pk):
    asist = Asistente.objects.filter(id=pk)
    serializer = AsistenteSerializador(asist, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def asisCreate(request):
    serializer = AsistenteSerializador(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def asisListDate(request):
    fechas = FechaInputSerializador(data=request.data)
    print(fechas)
    if fechas.is_valid():
        asist = Asistente.objects.filter(
        date_llegada__gte=fechas.data['fecha_inicio'], 
        date_llegada__lte=fechas.data['fecha_final'])
        serializer = AsistenteSerializador(asist, many=True)
        return Response(serializer.data)
    else:
        return Response({'error':'se necesitan fechas'})






