from rest_framework.serializers import ModelSerializer

from .models import Consulta,PrescricaoMedica,Agendamento,ExameSolicitado

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class AgendamentoSerializer(ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class ExameSerializer(ModelSerializer):
    class Meta:
        model = ExameSolicitado
        fields = '__all__'

class PrescricaoMedicaSerializer(ModelSerializer):
    class Meta:
        model = PrescricaoMedica
        fields= '__all__'
