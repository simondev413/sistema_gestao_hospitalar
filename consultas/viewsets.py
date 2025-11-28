from rest_framework.viewsets import ModelViewSet

from .serializer import ExameSerializer,ConsultaSerializer,AgendamentoSerializer,PrescricaoMedicaSerializer
from .models import Consulta,ExameSolicitado,Agendamento,PrescricaoMedica

class ConsultaViewSet(ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()

class AgendamentoViewSet(ModelViewSet):
    serializer_class = AgendamentoSerializer
    queryset = Agendamento.objects.all()

class ExameviewSets(ModelViewSet):
    serializer_class= ExameSerializer
    queryset = ExameSolicitado.objects.all()

class PrescricaoViewSet(ModelViewSet):
    serializer_class = PrescricaoMedicaSerializer
    queryset = PrescricaoMedica.objects.all()