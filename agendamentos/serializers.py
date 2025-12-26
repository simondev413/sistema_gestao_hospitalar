from rest_framework import serializers
from .models import Agendamento, DisponibilidadeMedico
from django.db.models import Q

from usuarios.models import Paciente, Medico
from usuarios.serializers import PacienteSerializer, MedicoSerializer


class AgendamentoSerializer(serializers.ModelSerializer):

    paciente_id =  serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(),
        source='paciente',
        write_only=True)

    paciente =  PacienteSerializer(read_only=True)

    doutor_id = serializers.PrimaryKeyRelatedField(
        queryset=Medico.objects.all(),
        source='doutor',
    write_only=True )
    
    doutor = MedicoSerializer(read_only=True)


    class Meta:
        model = Agendamento
        fields = '__all__'
        read_only_fields = ['status']


    def validate(self, data):
        instance = self.instance  

        paciente = data.get('paciente', getattr(instance, 'paciente', None))
        doutor = data.get('doutor', getattr(instance, 'doutor', None))
        data_consulta = data.get('data', getattr(instance, 'data', None))
        hora_inicio = data.get('hora_inicio', getattr(instance, 'hora_inicio', None))
        hora_fim = data.get('hora_fim', getattr(instance, 'hora_fim', None))
        tipo = data.get('agendamento_tipo', getattr(instance, 'agendamento_tipo', None))
        meeting_link = data.get('meeting_link', getattr(instance, 'meeting_link', None))

       
        if instance and instance.status in ['CONCLUIDA', 'CANCELADA']:
            raise serializers.ValidationError(
                'Agendamentos concluídos ou cancelados não podem ser alterados.'
            )

        
        if hora_inicio >= hora_fim:
            raise serializers.ValidationError(
                'A hora de início deve ser menor que a hora de fim.'
            )

      
        if tipo == 'ONLINE' and not meeting_link:
            raise serializers.ValidationError({
                'meeting_link': 'Consultas online exigem um link de reunião.'
            })

        
        conflitos = Agendamento.objects.filter(
            data=data_consulta
        )

        if instance:
            conflitos = conflitos.exclude(pk=instance.pk)

        
        conflito_paciente = conflitos.filter(
            paciente=paciente
        ).filter(
            Q(hora_inicio__lt=hora_fim) &
            Q(hora_fim__gt=hora_inicio)
        ).exists()

        if conflito_paciente:
            raise serializers.ValidationError(
                'O paciente já possui um agendamento que conflita com este horário.'
            )

        
        conflito_doutor = conflitos.filter(
            doutor=doutor
        ).filter(
            Q(hora_inicio__lt=hora_fim) &
            Q(hora_fim__gt=hora_inicio)
        ).exists()

        if conflito_doutor:
            raise serializers.ValidationError(
                'O doutor já possui um agendamento que conflita com este horário.'
            )

        
        dia_semana = data_consulta.weekday()

        disponibilidade = DisponibilidadeMedico.objects.filter(
            doutor=doutor,
            dia_semana=dia_semana,
            hora_inicio__lte=hora_inicio,
            hora_fim__gte=hora_fim,
            is_active=True
        ).exists()

        if not disponibilidade:
            raise serializers.ValidationError(
                'O doutor não está disponível neste horário.'
            )

        return data

class DisponibilidadeMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibilidadeMedico
        fields = '__all__'