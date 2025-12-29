from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from drf_yasg import openapi, views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import views,openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.views import logout_view,user_data

from usuarios.views import logout_view
from usuarios.auth_doc_view import LoginDocView, LogoutDocView
from usuarios.viewsets import (
    UsuarioViewSet,FuncionarioViewSet,
    MedicoViewSet,RecepcionistaViewSet,
    PacienteViewSet
    )

from usuarios.auth_doc_view import LoginDocView,LogoutDocView

from consultas.viewsets import ConsultaViewSet,ExameviewSets,PrescricaoViewSet

from agendamentos.viewsets import AgendamentoViewSet,DisponibilidadeMedicoViewSet
from dados_medicos.viewsets import HistoricoMedicoViewSet

from farmacia.viewsets import  SaidaMedicamentoViewSet,MedicamentoViewSet
from pagamentos.viewsets import PagamentoViewSet,FaturaViewSet,ReciboViewSet


routes = DefaultRouter()

schema_view = views.get_schema_view(
    openapi.Info(
        title='SGH API Documentação',
        default_version='v1',
        description='Esta é a documentação da API do SGH.',
        contact=openapi.Contact(email="devemail413@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

routes.register(r'usuarios',UsuarioViewSet,basename='usuarios')
routes.register(r'funcionarios',FuncionarioViewSet,basename='funcionarios')
routes.register(r'medicos',MedicoViewSet,basename='medicos')
routes.register(r'recepcionistas',RecepcionistaViewSet,basename='recepcionistas')
routes.register(r'pacientes',PacienteViewSet,basename='pacientes')
routes.register(r'consultas',ConsultaViewSet,basename='consultas')
routes.register(r'prescricoes',PrescricaoViewSet,basename='prescricoes')
routes.register(r'exames',ExameviewSets,basename='exames')
routes.register(r'agendamentos',AgendamentoViewSet,basename='agendamentos')
routes.register(r'disponibilidade-medico',DisponibilidadeMedicoViewSet,basename='disponibilidade-medico')
routes.register(r'historicos-medico',HistoricoMedicoViewSet,basename='historico-medico')
routes.register(r'medicamentos',MedicamentoViewSet,basename='medicamentos')
routes.register(r'saida-medicamentos',SaidaMedicamentoViewSet,basename='saida-medicamentos')
routes.register(r'pagamentos',PagamentoViewSet,basename='pagamentos')
routes.register(r'faturas',FaturaViewSet,basename='faturas')
routes.register(r'recibos',ReciboViewSet,basename='recibos')




urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/doc/<format>/', schema_view.without_ui(cache_timeout=0)),
    path('api/v1/doc/', schema_view.with_ui('swagger')),
    path('api/v1/redoc/', schema_view.with_ui('redoc')),

      # Autenticação JWT
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/logout/', logout_view, name='logout'),

    path('api/v1/me',user_data,name='user-metadata'),

    path('api/v1/auth/docs/login/', LoginDocView.as_view(), name='auth-login-doc'),
    path('api/v1/auth/docs/logout/', LogoutDocView.as_view(), name='auth-logout-doc'),

    path('api/v1/', include(routes.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
