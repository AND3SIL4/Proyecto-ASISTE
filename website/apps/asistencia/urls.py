from django.urls import path
from .views import Aprendices

urlpatterns = [
    path('aprendices', Aprendices.as_view(), name='lista_aprendices'), 
]
