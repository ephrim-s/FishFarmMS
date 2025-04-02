from rest_framework import generics, viewsets, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Pond, PondRental, Contract, FishGrowth, Expense, Commission, CommissionRate, InsurancePackage, FarmerInsurance
from .serializers import PondSerializer, PondRentalSerializer, ContractSerializer, FishGrowthSerializer, ExpenseSerializer, CommissionRateSerializer, CommissionSerializer, InsurancePackageSerializer, FarmerInsuranceSerializer
from core.permissions import IsWorkerOrAdmin, IsExternalFarmer

class FarmerDashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsExternalFarmer]

    def get(self, request):
        return Response({"message": "Welcome, External Farmer!"})
    
class PondViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pond.objects.filter(status='available')
    serializer_class = PondSerializer
    permission_classes = [permissions.AllowAny]

class PondRentalViewSet(viewsets.ModelViewSet):
    queryset = PondRental.objects.all()
    serializer_class = PondRentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        farmer = request.user
        pond_id = request.data.get('pond')
        pond = get_object_or_404(Pond, id=pond_id, status='available')

        rental = PondRental.objects.create(farmer=farmer, pond=pond)
        pond.status = 'rented'
        pond.save()

        return Response(PondRentalSerializer(rental).data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return PondRental.objects.all()
        return PondRental.objects.filter(farmer=self.request.user)
    
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        farmer = request.user
        rental_id = request.data.get('rental')
        rental = get_object_or_404(PondRental, id=rental_id, farmer=farmer)

        contract = Contract.objects.create(rental=rental, file=request.FILES['file'])
        return Response(ContractSerializer(contract).data, status=status.HTTP_201_CREATED)
    
class FishGrowthCreateView(generics.ListCreateAPIView):
    queryset = FishGrowth.objects.all()
    serializer_class = FishGrowthSerializer
    permission_classes = [IsWorkerOrAdmin]

    def perform_create(self, serializer):
        serializer.save()

class FishGrowthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FishGrowth.objects.all()
    serializer_class = FishGrowthSerializer
    permission_classes = [IsWorkerOrAdmin]

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsWorkerOrAdmin()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)

class CommissionRateView(generics.RetrieveUpdateAPIView):
    queryset = CommissionRate.objects.all()
    serializer_class = CommissionRateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return CommissionRate.get_current_rates()

class InsurancePackageViewSet(viewsets.ModelViewSet):
    queryset = InsurancePackage.objects.filter(is_active=True)
    serializer_class = InsurancePackageSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can manage packages

class FarmerInsuranceViewSet(viewsets.ModelViewSet):
    queryset = FarmerInsurance.objects.all()
    serializer_class = FarmerInsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)