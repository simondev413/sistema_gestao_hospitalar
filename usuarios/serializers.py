from rest_framework.serializers import ModelSerializer,HyperlinkedRelatedField
from .models import Usuario,Paciente,Medico,Funcionario,Recepcionista

from django.contrib.auth.models import Permission,Group




class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only':True},

        }

    def create(self, validated_data):
        user = Usuario(email=self.validated_data['email'])
        user.data_nascimento = self.validated_data['data_nascimento']
        user.set_password(self.validated_data['password'])
        user.save()

        group = validated_data['groups'][0]
        user.groups.set(Group.objects.filter(name=group))
        user.user_permissions.set(Permission.objects.filter(group=group))
        user.save()
        return user
    

class FuncionarioSerializer(ModelSerializer):
    usuario = HyperlinkedRelatedField(many=False,view_name='usuarios-detail',read_only=True)
    class Meta:
        model = Funcionario
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    funcionario = HyperlinkedRelatedField(many=False,view_name='funcionarios-detail',read_only=True)
    class Meta:
        model = Medico
        fields = '__all__'


class RecepcionistaSerializer(ModelSerializer):
    funcionario = HyperlinkedRelatedField(many=False,view_name='funcionarios-detail',read_only=True)
    class Meta:
        model = Recepcionista
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    usuario = HyperlinkedRelatedField(many=False,view_name='usuarios-detail',read_only=True)
    class Meta:
        model = Paciente
        fields = '__all__'