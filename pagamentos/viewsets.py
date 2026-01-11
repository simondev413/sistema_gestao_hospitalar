from rest_framework.viewsets import ModelViewSet
from .models import Pagamento, Fatura, Recibo
from .serializers import PagamentoSerializer, FaturaSerializer, ReciboSerializer
from rest_framework.permissions import IsAuthenticated


class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = []


class FaturaViewSet(ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
    permission_classes = []


class ReciboViewSet(ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer
    permission_classes = []
