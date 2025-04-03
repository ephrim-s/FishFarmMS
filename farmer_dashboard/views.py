from rest_framework import generics, viewsets, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Pond, PondRental, Contract, FishGrowth, Expense, Commission, CommissionRate, InsurancePackage, FarmerInsurance
from .serializers import PondSerializer, PondRentalSerializer, ContractSerializer, FishGrowthSerializer, ExpenseSerializer, CommissionRateSerializer, CommissionSerializer, InsurancePackageSerializer, FarmerInsuranceSerializer, PondCreateSerializer
from core.permissions import IsWorkerOrAdmin, IsExternalFarmer

class FarmerDashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsExternalFarmer]

    def get(self, request):
        return Response({"message": "Welcome, External Farmer!"})
    
class PondViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pond.objects.filter(status='available')
    serializer_class = PondSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Pond.objects.all()
        return Pond.objects.filter(status='available')

class AddOrViewPond(viewsets.ModelViewSet):
    queryset = Pond.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PondCreateSerializer
        return PondSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Only adin can add new ponds")
        serializer.save()

class PondRentalViewSet(viewsets.ModelViewSet):
    queryset = PondRental.objects.all()
    serializer_class = PondRentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        farmer = request.user
        pond_id = request.data.get('pond')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Start and end date are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        pond = get_object_or_404(Pond, id=pond_id, status='available')
        rental = PondRental.objects.create(farmer=farmer, pond=pond, start_date=start_date, end_date=end_date)
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
        serializer.save(recorded_by=self.request.user)

class FishGrowthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FishGrowth.objects.all()
    serializer_class = FishGrowthSerializer
    permission_classes = [IsWorkerOrAdmin]

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff: 
            return Expense.objects.all().order_by('-date')
        return Expense.objects.filter(farmer=user).order_by('-date')  
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(farmer=user, recorded_by=user)

class CommissionRateView(generics.RetrieveUpdateAPIView):
    queryset = CommissionRate.objects.all()
    serializer_class = CommissionRateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return CommissionRate.get_current_rates()

class InsurancePackageViewSet(viewsets.ModelViewSet):
    queryset = InsurancePackage.objects.filter(is_active=True)
    serializer_class = InsurancePackageSerializer
    permission_classes = [permissions.IsAdminUser] 

class FarmerInsuranceViewSet(viewsets.ModelViewSet):
    queryset = FarmerInsurance.objects.all()
    serializer_class = FarmerInsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)