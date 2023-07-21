from rest_framework import status, permissions, generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import * 
from .permissions import *
from .models import *
# Create your views here.
# Vistas publicas
class AprendicesListViews(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Aprendiz.objects.all().exists():

            aprendiz = Aprendiz.objects.all()
            serializer = AprendizSerializer(aprendiz, many=True)
            return Response({'aprendices':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'No se encontraron aprendices'}, status=status.HTTP_404_NOT_FOUND)

class AprendicesViewByDocument(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        documento_aprendiz = request.query_params.get('documento_aprendiz')
        if documento_aprendiz:
            try:
                aprendiz = Aprendiz.objects.get(documento_aprendiz=documento_aprendiz)
                serializer = AprendizSerializer(aprendiz)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Aprendiz.DoesNotExist:
                return Response({'error': 'Aprendiz no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Parámetro "documento_aprendiz" no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

# Vistas privadas























# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .models import Aprendiz, Instructor, Administrativo
# from .serializers import AprendizSerializer, InstructorSerializer, AdministrativoSerializer

# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, format=None):
#         # Implementa aquí la lógica de inicio de sesión y generación del token de autenticación
#         # ...
#         return Response({'token': 'token_generado'}, status=status.HTTP_200_OK)

# class UserProfileView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         user = request.user
#         if user.user_type == 'Aprendiz':
#             profile = Aprendiz.objects.get(user=user)
#             serializer = AprendizSerializer(profile)
#         elif user.user_type == 'Instructor':
#             profile = Instructor.objects.get(user=user)
#             serializer = InstructorSerializer(profile)
#         elif user.user_type == 'Administrativo':
#             profile = Administrativo.objects.get(user=user)
#             serializer = AdministrativoSerializer(profile)
#         else:
#             return Response({'error': 'Tipo de usuario no válido'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(serializer.data, status=status.HTTP_200_OK)

# class AprendicesListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         if request.user.user_type == 'Instructor':
#             aprendices = Aprendiz.objects.filter(instructor=request.user.instructor)
#             serializer = AprendizSerializer(aprendices, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'No tienes permisos para acceder a esta vista'}, status=status.HTTP_403_FORBIDDEN)

# Implementa las demás vistas según tus necesidades
# ...




# Ejemplo de renderizacion por tipo de usuario
# def user_detail(request, user_id):
#     user = CustomUser.objects.get(id=user_id)
#     if user.user_type == 'aprendiz':
#         user_info = Aprendiz.objects.get(user=user)
#     elif user.user_type == 'instructor':
#         user_info = Instructor.objects.get(user=user)
#     # Agrega más condiciones para otros tipos de usuario si es necesario

#     return render(request, 'user_detail.html', {'user': user, 'user_info': user_info})