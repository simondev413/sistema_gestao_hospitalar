from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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

    @action(detail=False, methods=['post'], url_path='reset-senha')
    def reset_senha(self, request):
        user_id = request.data.get('user_id')
        nova_senha = request.data.get('nova_senha')

        if not user_id or not nova_senha:
            return Response(
                {'erro': 'user_id e senha são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = Usuario.objects.get(id=user_id)
        except Usuario.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado'}, status=404)

        user.set_password(nova_senha)
        user.save()

        return Response({'mensagem': 'Senha redefinida com sucesso'})


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

