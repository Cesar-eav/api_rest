from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Tarea 
from .serializers import TareaSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
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
    def list(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 3  # tamaño fijo aquí
        qs = self.get_queryset().order_by("id")
        page = paginator.paginate_queryset(qs, request)
        ser = self.get_serializer(page, many=True)
        return paginator.get_paginated_response(ser.data) 