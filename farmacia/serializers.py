from rest_framework import serializers
from .models import Medicamento, SaidaMedicamento

from usuarios.models import Paciente, Funcionario
from usuarios.serializers import PacienteSerializer, FuncionarioSerializer


class MedicamentoSerializer(serializers.ModelSerializer):
    estoque_baixo = serializers.BooleanField(read_only=True)

    class Meta:
        model = Medicamento
        fields = '__all__'


class SaidaMedicamentoSerializer(serializers.ModelSerializer):

    medicamento_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicamento.objects.all(),
        source='medicamento',
        write_only=True)
    medicamento = MedicamentoSerializer(read_only=True)

    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(),
        source='paciente',
        write_only=True)
    
    paciente = PacienteSerializer(read_only=True)

    fucionario_id = serializers.PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(),
        source='funcionario',
        write_only=True)    
    
    funcionario = FuncionarioSerializer(read_only=True)

    class Meta:
        model = SaidaMedicamento
        fields = '__all__'

    def validate(self, data):
        medicamento = data['medicamento']
        quantidade = data['quantidade']

        if not medicamento.ativo:
            raise serializers.ValidationError("Medicamento inativo.")

        if medicamento.estoque_atual < quantidade:
            raise serializers.ValidationError("Estoque insuficiente.")

        return data

    def create(self, validated_data):
        medicamento = validated_data['medicamento']
        quantidade = validated_data['quantidade']

        medicamento.estoque_atual -= quantidade
        medicamento.save()

        return super().create(validated_data)
