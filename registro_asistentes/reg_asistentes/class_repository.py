from rest_framework.serializers import Serializer
from .serializer import AsistenteSerializador
from .serializer import FechaInputSerializador
from .models import Asistente

class AsistenteRepository():

    """ Listar todos by nombre """
    def listByName(self):
        asist = Asistente.objects.all().order_by('nombres')
        serializer = AsistenteSerializador(asist, many=True)

        for item in serializer.data:
            item.pop('correo_electronico')

        return serializer.data

    """ Listar rango de fecha """
    def listBtwDate(self, request):
        fechas = FechaInputSerializador(data=request.data)
        print(fechas)
        if fechas.is_valid():

            asist = Asistente.objects.filter(
            date_llegada__gte=fechas.data['fecha_inicio'], 
            date_llegada__lte=fechas.data['fecha_final'])

            serializer = AsistenteSerializador(asist, many=True)

            for item in serializer.data:
                item.pop('correo_electronico')

            return serializer.data
        else:
            return {'error':'se necesitan fechas'}

    """ Agregar """
    def CreateAsis(self, request):
        serializer = AsistenteSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return serializer.data


    """ Obtener Detalles """
    def detailsById(self, pk):
        asist = Asistente.objects.filter(id=pk)
        serializer = AsistenteSerializador(asist, many=True)

        for item in serializer.data:
            item.pop('correo_electronico')

        return serializer.data
