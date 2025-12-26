from rest_framework.viewsets import ModelViewSet
from .models import Medicamento, SaidaMedicamento
from .serializers import MedicamentoSerializer, SaidaMedicamentoSerializer
from rest_framework.permissions import IsAuthenticated


class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = []


class SaidaMedicamentoViewSet(ModelViewSet):
    queryset = SaidaMedicamento.objects.all()
    serializer_class = SaidaMedicamentoSerializer
    permission_classes = []
