from django.db import models
from rest_framework import serializers
from .models import Asistente

class AsistenteSerializador(serializers.ModelSerializer):
    class Meta:
        model = Asistente
        fields = '__all__'