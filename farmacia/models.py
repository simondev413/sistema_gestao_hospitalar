from django.db import models
from usuarios.models import Paciente, Funcionario


class Medicamento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    unidade_medida = models.CharField(max_length=50)
    estoque_atual = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def estoque_baixo(self):
        return self.estoque_atual <= self.estoque_minimo

    def __str__(self):
        return self.nome


class SaidaMedicamento(models.Model):

    TIPO_SAIDA = (
        ('PACIENTE', 'Paciente Internado'),
        ('PRESCRICAO', 'Prescrição'),
    )

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.PROTECT,
        related_name='saidas'
    )
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT
    )
    quantidade = models.PositiveIntegerField()
    tipo_saida = models.CharField(max_length=20, choices=TIPO_SAIDA)
    data_saida = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.medicamento} - {self.quantidade}'
