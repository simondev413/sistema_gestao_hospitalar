from rest_framework.routers import DefaultRouter
from .viewsets import MedicamentoViewSet, SaidaMedicamentoViewSet

router = DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'saidas-medicamentos', SaidaMedicamentoViewSet)

urlpatterns = router.urls
