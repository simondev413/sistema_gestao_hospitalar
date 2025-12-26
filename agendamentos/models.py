from django.db import models

class Agendamento(models.Model):

    AGENDAMENTO_CHOICES = (
        ('ONLINE', 'Online'),
        ('PRESENCIAL', 'Presencial'),
    )

    STATUS_CHOICES = (
        ('AGENDADA', 'Agendada'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('CONCLUIDA', 'Concluída'),
    )

    paciente = models.ForeignKey(
        'usuarios.Paciente',
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doutor = models.ForeignKey(
        'usuarios.Medico',
        on_delete=models.CASCADE,
        related_name='doctor_appointments'
    )

    agendamento_tipo= models.CharField(
        max_length=15,
        choices=AGENDAMENTO_CHOICES
    )

    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='AGENDADA'
    )

    meeting_link = models.URLField(
        blank=True,
        null=True
    )

    criado_aos = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data', 'hora_inicio']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

        constraints = [
            models.UniqueConstraint(
                fields=['doutor', 'data', 'hora_inicio'],
                name='agendamento_unico_doutor'
            ),
        ]

    def __str__(self):
        return f'{self.paciente} - {self.data} {self.hora_inicio}'

class DisponibilidadeMedico(models.Model):
    DIA_SEMANAS = (
        (0, 'Segunda'),
        (1, 'Terça'),
        (2, 'Quarta'),
        (3, 'Quinta'),
        (4, 'Sexta'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    doutor = models.ForeignKey(
        'usuarios.Medico',
        on_delete=models.CASCADE,
        related_name='availabilities'
    )

    dia_semana = models.IntegerField(choices=DIA_SEMANAS)

    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    is_active = models.BooleanField(default=True)

    criado_aos = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Disponibilidade do Médico'
        verbose_name_plural = 'Disponibilidades dos Médicos'

    def mostrar_dia_semana(self):
        return self.dia_semana

    def __str__(self):
        return f'{self.doutor} - {self.mostrar_dia_semana()}'
