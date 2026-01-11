from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Consulta,PrescricaoMedica,ExameSolicitado

from usuarios.models import Medico,Paciente
from usuarios.serializers import MedicoSerializer,PacienteSerializer
from agendamentos.models import Agendamento
from agendamentos.serializers import AgendamentoSerializer



class ConsultaSerializer(ModelSerializer):
    agendamento_id = PrimaryKeyRelatedField(
        queryset=Agendamento.objects.all(),write_only=True,source='agendamento'
    )
    agendamento = AgendamentoSerializer(read_only=True)

    class Meta:
        model = Consulta
        fields = '__all__'

class ExameSerializer(ModelSerializer):
    class Meta:
        model = ExameSolicitado
        fields = '__all__'

class PrescricaoMedicaSerializer(ModelSerializer):
    class Meta:
        model = PrescricaoMedica
        fields= '__all__'
