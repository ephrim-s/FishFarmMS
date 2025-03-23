from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, PondViewSet, PondRentalViewSet, FishGrowthCreateView, FishGrowthDetailView, FarmerDashboardView

router = DefaultRouter()
router.register(r'ponds', PondViewSet) 
router.register(r'pond-rentals', PondRentalViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('dashboard/', FarmerDashboardView.as_view(), name='farmer-dashboard'),
    path('fish-growth/', FishGrowthCreateView.as_view(), name='fish-growth'), 
    path('fish-growth/<int:pk>/', FishGrowthDetailView.as_view(), name='fish-growth-detail'),
]