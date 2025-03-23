from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, PondViewSet, PondRentalViewSet, FishGrowthCreateView, FishGrowthDetailView, FarmerDashboardView, ExpenseListCreateView, CommissionRateView, InsurancePackageViewSet, FarmerInsuranceViewSet

router = DefaultRouter()
router.register(r'ponds', PondViewSet) 
router.register(r'pond-rentals', PondRentalViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'insurance-packages', InsurancePackageViewSet)
router.register(r'farmer-insurance', FarmerInsuranceViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('dashboard/', FarmerDashboardView.as_view(), name='farmer-dashboard'),
    path('fish-growth/', FishGrowthCreateView.as_view(), name='fish-growth'), 
    path('fish-growth/<int:pk>/', FishGrowthDetailView.as_view(), name='fish-growth-detail'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('commission-rate/', CommissionRateView.as_view(), name='commission-rate'),
]