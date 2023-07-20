from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView
from .models import *

# Create your views here.
from rest_framework import generics
class Aprendices(generics.ListAPIView):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer
    permission_classes = (permissions.AllowAny,)


# class Aprendices(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, format=None):
#         if Aprendiz.objects.all().exists():
#             aprendices = Aprendiz.objects.all()
#             return Response({'aprendices':'test message'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error':'No aprendices found'}, status=status.HTTP_404_NOT_FOUND)

# class CustomUserListView(ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class InstructorListView(ListAPIView):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer


        
        # serializer = serializers.ListaAprendizesSerializer(aprendizs, many=True)
        # return Response({'data':serializer.data})


    # Ejemplo de renderizacion por tipo de usuario
    # def user_detail(request, user_id):
    #     user = CustomUser.objects.get(id=user_id)
    #     if user.user_type == 'aprendiz':
    #         user_info = Aprendiz.objects.get(user=user)
    #     elif user.user_type == 'instructor':
    #         user_info = Instructor.objects.get(user=user)
    #     # Agrega más condiciones para otros tipos de usuario si es necesario

    #     return render(request, 'user_detail.html', {'user': user, 'user_info': user_info})