from rest_framework.viewsets import ModelViewSet
from .serializers import (
    UsuarioSerializer,Usuario,
    FuncionarioSerializer,Funcionario,
    MedicoSerializer,Medico,
    RecepcionistaSerializer,Recepcionista,
    PacienteSerializer,Paciente
    )


class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class MedicoViewSet(ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()


class FuncionarioViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()


class RecepcionistaViewSet(ModelViewSet):
    serializer_class = RecepcionistaSerializer
    queryset = Recepcionista.objects.all()


class PacienteViewSet(ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

