from rest_framework import serializers
from apps.asistencia.serializers import AprendizSerializer
from .models import *

class NovedadSerializer(serializers.ModelSerializer):
    documento_aprendiz = AprendizSerializer()
    class Meta:
        model = Novedad
        fields = '__all__'




