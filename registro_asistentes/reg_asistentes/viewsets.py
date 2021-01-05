from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializer
from rest_framework.response import Response

class AsistenteViewSet(viewsets.ModelViewSet):
    queryset = models.Asistente.objects.all()
    serializer_class = serializer.AsistenteSerializador

    # list(), retrive(), update(), destroy()