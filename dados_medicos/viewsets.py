from rest_framework.viewsets import ModelViewSet
from .serializers import HistoricoMedico,HistoricoMedicoSerializer

class HistoricoMedicoViewSet(ModelViewSet):
    serializer_class = HistoricoMedicoSerializer
    queryset = HistoricoMedico.objects.all()