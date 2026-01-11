from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,ValidationError #type:ignore
from .models import Usuario,Paciente,Medico,Funcionario,Recepcionista


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only':True},

        }

    def create(self, validated_data:dict[str,str]):
        user = Usuario(email=self.validated_data['email']) #type:ignore
        user.nome = self.validated_data['nome'] #type:ignore
        user.sobrenome = self.validated_data['sobrenome'] #type:ignore
        user.telefone = self.validated_data['telefone'] #type:ignore
        user.tipo = self.validated_data['tipo'] #type:ignore
        user.data_nascimento = self.validated_data['data_nascimento'] #type:ignore
        user.genero = self.validated_data['genero'] #type:ignore
        user.img = self.validated_data['img'] #type:ignore
        user.set_password(self.validated_data['password']) #type:ignore
        user.save()
        return user
    

class FuncionarioSerializer(ModelSerializer):
    usuario_id = PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='usuario',
        write_only=True
    )

    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Funcionario
        fields = '__all__'
  
class MedicoSerializer(ModelSerializer):
    
    funcionario_id = PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(),
        source='funcionario',
        write_only=True
    )


    funcionario = FuncionarioSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = '__all__'


class RecepcionistaSerializer(ModelSerializer):
    
    funcionario_id = PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(),
        source='funcionario',
        write_only=True
    )

    
    funcionario = FuncionarioSerializer(read_only=True)

    class Meta:
        model = Recepcionista
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    # 👉 entrada
    usuario_id = PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='usuario',
        write_only=True
    )

    # 👉 saída
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'