from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, PondViewSet, PondRentalViewSet

router = DefaultRouter()
router.register(r'ponds', PondViewSet)
router.register(r'pond-rentals', PondRentalViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
]
