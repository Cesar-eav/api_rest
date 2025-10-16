from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Tarea 
from .serializers import TareaSerializer
# Create your views here.




class TareaViewSet(viewsets.ModelViewSet):
    """
    API RESTful para gestionar Mascotas.
    Métodos disponibles:
    - GET /api/mascotas/ → listar
    - POST /api/mascotas/ → crear
    - GET /api/mascotas/{id}/ → obtener detalle
    - PUT/PATCH /api/mascotas/{id}/ → actualizar
    - DELETE /api/mascotas/{id}/ → eliminar
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer     
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo']
    ordering_fields = ['titulo']
 