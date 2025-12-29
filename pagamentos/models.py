from django.db import models
from agendamentos.models import Agendamento
from usuarios.models import Paciente


class Pagamento(models.Model):

    METODO_PAGAMENTO = (
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão'),
        ('TRANSFERENCIA', 'Transferência'),
    )

    STATUS = (
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('CANCELADO', 'Cancelado'),
    )

    consulta = models.OneToOneField(
        Agendamento,
        on_delete=models.CASCADE,
        related_name='pagamento'
    )
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=20, choices=METODO_PAGAMENTO)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDENTE')
    data_pagamento = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pagamento {self.id} - {self.status}'

class Fatura(models.Model):
    pagamento = models.OneToOneField(
        Pagamento,
        on_delete=models.CASCADE,
        related_name='fatura'
    )
    numero_fatura = models.CharField(max_length=100, unique=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_fatura


class Recibo(models.Model):
    pagamento = models.OneToOneField(
        Pagamento,
        on_delete=models.CASCADE,
        related_name='recibo'
    )
    numero_recibo = models.CharField(max_length=100, unique=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_recibo
