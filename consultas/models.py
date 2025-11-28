from django.db import models

# Create your models here.

class Consulta(models.Model):
  
    STATUS = {
        'realizada':'Realizada',
        'pendente':'Pendente',
        'cancelada':'Cancelada',
    }
    
    diagnostico = models.TextField(max_length=500)
    status = models.CharField(max_length=15,choices=STATUS)
    data_consulta = models.DateTimeField(blank=True,null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    agendamento = models.OneToOneField('consultas.Agendamento',on_delete=models.CASCADE)

class Agendamento(models.Model):
    MODELO_CHOICES = {
        'presencial':'Presencial',
        'online':'Online'
    }
    
    STATUS = {
        'agendado':'Agendado',
        'em espera':'Em espera'
    }

    motivo = models.TextField(max_length=500)
    data_consulta = models.DateTimeField(null=True,blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    modelo = models.CharField(max_length=12,choices=MODELO_CHOICES)
    profisional = models.ForeignKey('usuarios.Medico',on_delete=models.CASCADE)
    paciente = models.ForeignKey('usuarios.Paciente',on_delete=models.CASCADE)

class ExameSolicitado(models.Model):
    STATUS = {
        'realizado':'Realizado',
        'nao realizado':'Não Realizado'
    }


    nome_exame = models.CharField(max_length=60)
    descricao = models.TextField(max_length=500)
    status = models.CharField(max_length=15,choices=STATUS)
    consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_resultado = models.DateTimeField()
    

class PrescricaoMedica(models.Model):
    medicamento = models.CharField(max_length=45)
    dosagem = models.CharField(max_length=45)
    frequencia = models.CharField(max_length=45)
    duracao = models.CharField(max_length=45)
    observacao = models.TextField(max_length=500)
    data_prescricao = models.DateTimeField(auto_now_add=True)
    consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)