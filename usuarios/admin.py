from django.contrib import admin
from .models import (
    Usuario,Medico,
    Paciente,Recepcionista,
    Funcionario)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Recepcionista)