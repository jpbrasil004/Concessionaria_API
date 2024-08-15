from rest_framework.serializers import ModelSerializer
from .models import Montadora, Modelo

class MontadoraSerializer(ModelSerializer):

    class Meta:
        model = Montadora
        fields = '__all__'

class ModeloSerializer(ModelSerializer):
    montadora = MontadoraSerializer(many=False, read_only=True)

    class Meta:
        model = Modelo
        fields = '__all__'