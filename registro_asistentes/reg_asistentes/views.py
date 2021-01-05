from rest_framework.decorators import api_view
from rest_framework.response import Response
from .class_repository import AsistenteRepository

AsistenteRpObj = AsistenteRepository()


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
    AllDataByName = AsistenteRpObj.listByName()
    return Response(AllDataByName)

@api_view(['GET'])
def asisDetail(request, pk):
    OneDataByPk = AsistenteRpObj.detailsById(pk)
    return Response(OneDataByPk)


@api_view(['POST'])
def asisCreate(request):
    CreateResult = AsistenteRpObj.CreateAsis(request)
    return Response(CreateResult)

@api_view(['POST'])
def asisListDate(request):
    AllDataByDates = AsistenteRpObj.listBtwDate(request)
    return Response(AllDataByDates)






