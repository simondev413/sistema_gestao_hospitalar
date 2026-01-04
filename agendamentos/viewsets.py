from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Agendamento,DisponibilidadeMedico
from .serializers import AgendamentoSerializer,DisponibilidadeMedicoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = []

    def get_queryset(self):
        """
        Filtro básico:
        - Paciente vê seus agendamentos
        - Doutor vê sua agenda
        - Admin vê tudo
        """
        user = self.request.user

        qs = Agendamento.objects.all()  

        if hasattr(user, 'paciente'):
            return self.queryset.filter(paciente=user.paciente)

        if hasattr(user, 'medico'):
            return self.queryset.filter(doutor=user.medico)

        return qs 

    def get_paginated_response(self, data):
        return Response(data)
   
    def create(self, request, *args, **kwargs):
        """
        Criação de agendamento
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['patch'], url_path='confirmar')
    def confirmar_agendamento(self, request, pk=None):
        agendamento = self.get_object()

        if agendamento.status != 'AGENDADA':
            return Response(
                {'detail': 'Apenas agendamentos AGENDADOS podem ser confirmados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        agendamento.status = 'CONFIRMADA'
        agendamento.save(update_fields=['status'])

        return Response(
            {'detail': 'Agendamento confirmado com sucesso.'},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['patch'], url_path='cancelar')
    def cancelar_agendamento(self, request, pk=None):
        agendamento = self.get_object()

        if agendamento.status == 'CONCLUIDA':
            return Response(
                {'detail': 'Agendamentos concluídos não podem ser cancelados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        agendamento.status = 'CANCELADA'
        agendamento.save(update_fields=['status'])

        return Response(
            {'detail': 'Agendamento cancelado com sucesso.'},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['patch'], url_path='concluir')
    def concluir_agendamento(self, request, pk=None):
        agendamento = self.get_object()

        if agendamento.status != 'CONFIRMADA':
            return Response(
                {'detail': 'Apenas consultas confirmadas podem ser concluídas.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        agendamento.status = 'CONCLUIDA'
        agendamento.save(update_fields=['status'])

        return Response(
            {'detail': 'Consulta concluída.'},
            status=status.HTTP_200_OK
        )

class DisponibilidadeMedicoViewSet(viewsets.ModelViewSet):
    serializer_class = DisponibilidadeMedicoSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = DisponibilidadeMedico.objects.filter(is_active=True)
        doutor_id = self.request.query_params.get('doutor')

        if doutor_id:
            queryset = queryset.filter(doutor_id=doutor_id)

        return queryset
