from rest_framework import serializers
from .models import Pagamento, Fatura, Recibo
from django.utils import timezone
import uuid

from usuarios.models import Paciente
from usuarios.serializers import PacienteSerializer

from agendamentos.models import Agendamento
from agendamentos.serializers import AgendamentoSerializer

class PagamentoSerializer(serializers.ModelSerializer):

    consulta_id = serializers.PrimaryKeyRelatedField(
        queryset=Agendamento.objects.all(),
        source='consulta',
        write_only=True)
    consulta = AgendamentoSerializer(read_only=True)

    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(),
        source='paciente',
        write_only=True)
    
    paciente = PacienteSerializer(read_only=True)
    

    class Meta:
        model = Pagamento
        fields = '__all__'

    def update(self, instance, validated_data):
        status = validated_data.get('status')

        if status == 'PAGO' and instance.status != 'PAGO':
            instance.data_pagamento = timezone.now()

            Fatura.objects.get_or_create(
                pagamento=instance,
                defaults={
                    'numero_fatura': str(uuid.uuid4()),
                    'valor_total': instance.valor
                }
            )

            Recibo.objects.get_or_create(
                pagamento=instance,
                defaults={
                    'numero_recibo': str(uuid.uuid4()),
                    'valor_pago': instance.valor
                }
            )

        return super().update(instance, validated_data)


class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = '__all__'


class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibo
        fields = '__all__'
