from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'hecho', 'created_at']
        read_only_fields = ["id", "created_at"]

        def validate_titulo(self, value):
            if not value or not value.strip():
                raise serializers.ValidationError("El título es requerido.")
            return value.strip()
