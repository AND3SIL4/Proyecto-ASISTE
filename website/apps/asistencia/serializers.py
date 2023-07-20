from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CoordinacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coodinacion
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class ProgramaSerializer(serializers.ModelSerializer):
    coordinacion_programa = CoordinacionSerializer()
    class Meta:
        model = Programa
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class FichaSerializer(serializers.ModelSerializer):
    horario_ficha = HorarioSerializer(many=True)
    instructor_ficha = InstructorSerializer(many=True)
    programa_ficha = ProgramaSerializer()

    class Meta:
        model = Ficha
        fields = '__all__'

class AprendizSerializer(serializers.ModelSerializer):
    ficha_aprendiz = FichaSerializer()
    user_details = CustomUserSerializer(source='user', read_only=True)
    class Meta:
        model = Aprendiz
        fields = '__all__'

class NovedadSerializer(serializers.ModelSerializer):
    aprendiz = AprendizSerializer()
    documento_aprendiz = serializers.CharField(source='aprendiz.documento_aprendiz')

    class Meta:
        model = Novedad
        fields = '__all__'





