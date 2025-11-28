from django.contrib import admin
from .models import Consulta,PrescricaoMedica,ExameSolicitado,Agendamento

# Register your models here.
admin.site.register(Consulta)
admin.site.register(PrescricaoMedica)
admin.site.register(ExameSolicitado)
admin.site.register(Agendamento)