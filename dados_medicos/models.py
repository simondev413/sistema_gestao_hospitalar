from django.db import models

# Create your models here.
class HistoricoMedico(models.Model):
    doencas_previas = models.TextField(max_length=200)
    alergias = models.TextField(max_length=200)
    cirugias = models.TextField(max_length=200)
    tratamentos = models.TextField(max_length=200)
    observacoes = models.TextField(max_length=200)
    paciente = models.OneToOneField('usuarios.Paciente',on_delete=models.CASCADE)