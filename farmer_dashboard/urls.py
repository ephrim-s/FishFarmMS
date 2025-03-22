from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, PondViewSet, PondRentalViewSet, FishGrowthCreateView, FishGrowthDetailView

router = DefaultRouter()
router.register(r'', PondViewSet)
router.register(r'pond-rentals', PondRentalViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('fish-growth', FishGrowthCreateView.as_view(), name='fish-growth'), 
    path("fish-growth/<int:pk>/", FishGrowthDetailView.as_view(), name="fish-growth-detail"),
]
