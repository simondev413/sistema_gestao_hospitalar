from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField #type:ignore
from usuarios.models import Paciente
from .models import HistoricoMedico
from usuarios.serializers import PacienteSerializer

class HistoricoMedicoSerializer(ModelSerializer):
    paciente_id = PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(),write_only=True,source='paciente'
    )
    paciente = PacienteSerializer(read_only=True)   
    class Meta:
        model = HistoricoMedico
        fields = '__all__'

        