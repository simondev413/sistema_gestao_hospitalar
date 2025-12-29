from rest_framework.viewsets import ModelViewSet

from .serializer import ExameSerializer,ConsultaSerializer,PrescricaoMedicaSerializer
from .models import Consulta,ExameSolicitado,PrescricaoMedica


class ConsultaViewSet(ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()


class ExameviewSets(ModelViewSet):
    serializer_class= ExameSerializer
    queryset = ExameSolicitado.objects.all()

class PrescricaoViewSet(ModelViewSet):
    serializer_class = PrescricaoMedicaSerializer
    queryset = PrescricaoMedica.objects.all()