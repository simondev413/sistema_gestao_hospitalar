from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Group,Permission)





# Aqui criamos as entidades de Usuários
class UsuarioManager(BaseUserManager):
    def create_user(self,email,password = None,**extra_fields):
        if not email:
            raise ValueError("O E-mail é obrigatório.")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active',True)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password = None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
         
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser deve ter is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser deve ter is_superuser=True.')

        
        return self.create_user(email,password,**extra_fields)
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    """
    Model genérico para todo usuário do sistema
    """
    GENERO_CHOICES = {
        ('M','Masculino'),
        ('F','Feminino')
    }
    TIPO_CHOICES = {
        ('admin','Administrador'),
        ('funcionario','Funcionário'),
        ('paciente','Paciente')
    }

    nome = models.CharField(max_length=45,verbose_name='Primeiro Nome')
    sobrenome = models.CharField(max_length=45,verbose_name='Sobrenome')
    telefone = models.CharField(max_length=13,verbose_name='Contacto Telefónico')
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=15,choices=TIPO_CHOICES)
    genero = models.CharField(max_length=12,choices=GENERO_CHOICES)
    img = models.ImageField(upload_to=f'statics/imgs/usuarios',null=True,blank=True)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento',null=True,blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True,verbose_name='Usuário Ativo')
    is_staff = models.BooleanField(default=False,verbose_name='Usuário Funcionário')
    is_superuser = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(Group, related_name="custom_usuario_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_usuario_permissions_set", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','sobrenome']

    objects = UsuarioManager()

    def mostar_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    def obter_idade(self):
        idade = self.data_nascimento - timezone.now()
        return idade
    
    def __str__(self):
        return self.mostar_nome_completo()

class Funcionario(models.Model):
    """
    Model genérico para todo funcionario hospitalar (recepcionistas,médicos,enfermeiros, etc.)
    
    """
    CARGOS_CHOICES = {
        'administrativo':'Administrativo',
        'enfermeiro':'Enfermeiro',
        'farmaceutico':'Farmaceútico',
        'gestor':'Gestor',
        'medico':'Médico',
        'recepcionista':'Recepcionista',
        'tecnico':'Técnico',

    }
    
    DEPARTAMENTOS = {
        'recepcao':'Recepção',
        'cardiologia':'Cardiologia',
        'farmacia':'Farmácia',
        'laboratorio':'Laboratório'
    }
    TURNOS_CHOICES = {
        'manhã':'Manhã',
        'tarde':'Tarde',
        'noite':'Noite',
        'rotativo':'Rotativo'
    }
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE,limit_choices_to={'tipo':'funcionario'})
    cargo = models.CharField(max_length=20,choices=CARGOS_CHOICES)
    departamento = models.CharField(max_length=20,choices=DEPARTAMENTOS)
    data_admissao = models.DateField(auto_now=False,verbose_name='Data de admissão')
    data_demissao = models.DateTimeField(auto_now=False,null=True,blank=True,verbose_name='Data de demissão')
    nif = models.CharField(max_length=15,verbose_name='Número de identificação fiscal')
    turno = models.CharField(max_length=10,choices=TURNOS_CHOICES)
    anos_experiencia = models.SmallIntegerField(verbose_name='Anos de experiência',default=0)


    def __str__(self):
        return self.usuario.mostar_nome_completo()
    

class Medico(models.Model):
    ESPECIALIDADE_CHOICES = {
        'cardiologia':'Cardiologia',
        'pediatria':'Pediatria',
        'clinica_geral':'Clínica Geral'
    }
    funcionario = models.OneToOneField(Funcionario,on_delete=models.CASCADE,limit_choices_to={'cargo':'medico' or 'Médico'})
    especialidade = models.CharField(max_length=30)
    num_ordem_medicos = models.CharField(max_length=50,verbose_name='Número da ordem dos médicos')

    
    def __str__(self):
        return self.funcionario.usuario.mostar_nome_completo()

class Recepcionista(models.Model):
    POSTOS_CHOICES = {
        'principal':'Principal',
        'emergencia':'Emergência',
        'exames':'Exames',
        'internamento':'Internamento'
    }

    funcionario = models.OneToOneField(Funcionario,on_delete=models.CASCADE)
    posto_atendimento = models.CharField(max_length=30,choices=POSTOS_CHOICES)
    
    def __str__(self):
        return self.funcionario.usuario.mostar_nome_completo()

class Paciente(models.Model):
    TIPO_SANGUINEO_CHOICES = {
        'a+':'+A',
        'a-':'A-',
        'b-':'B-',
        'ab+':'AB+',
        'ab-':'AB-',
        'o+':'O+',
        'o-':'O-'
        
    }

    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)
    cod_medico = models.CharField(max_length=32,verbose_name='Código único de identificação do paciente ')
    tipo_sanguineo = models.CharField(max_length=20,choices=TIPO_SANGUINEO_CHOICES)
    peso = models.DecimalField(max_digits=5,decimal_places=2)
    altura = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.usuario.mostar_nome_completo()

