"""
URL configuration for sgh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


admin.site.site_title = ' '
admin.site.site_header = 'Administração do Sistema de Gestão Hospitalar'
admin.site.name = ' '
admin.site.index_title = 'Sistema de Gestão Hospitalar'

from rest_framework.routers import DefaultRouter
from drf_yasg import views,openapi

from usuarios.viewsets import (
    UsuarioViewSet,FuncionarioViewSet,
    MedicoViewSet,RecepcionistaViewSet,
    PacienteViewSet
    )


routes = DefaultRouter()

schema_view = views.get_schema_view(
    openapi.Info(
        title='SGH API Documentação',
        description='Esta é a documentção da API do sistema de Gestão Hospitalar, com todods os endpoints disponiveis.',
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="devemail413@gmail.com.com"),
        license=openapi.License(name="BSD License"),
    )
)

routes.register(r'usuarios',UsuarioViewSet,basename='usuarios')
routes.register(r'funcionarios',FuncionarioViewSet,basename='funcionarios')
routes.register(r'medicos',MedicoViewSet,basename='medicos')
routes.register(r'recepcionistas',RecepcionistaViewSet,basename='recepcionistas')
routes.register(r'pacientes',PacienteViewSet,basename='pacientes')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Documentação Swagger e Redoc
    path('api/v1/doc/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/auth/',include('rest_framework.urls'),name='api-auth'),
    path('api/v1/',include(routes.urls),name='drf_api')
]
