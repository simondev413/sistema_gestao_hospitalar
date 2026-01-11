from django.contrib import admin
from .models import Agendamento, DisponibilidadeMedico

# Register your models here.
admin.site.register(Agendamento)
admin.site.register(DisponibilidadeMedico)