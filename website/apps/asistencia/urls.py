from django.urls import path
from .views import *

urlpatterns = [
    path('aprendices', AprendicesListViews.as_view(), name='aprendices'), 
    path('aprendiz', AprendicesViewByDocument.as_view(), name='aprendices'), 
]
