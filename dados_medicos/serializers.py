from rest_framework.serializers import ModelSerializer
from .models import HistoricoMedico

class HistoricoMedicoSerializer(ModelSerializer):
    class Meta:
        model = HistoricoMedico
        fields = '__all__'

        