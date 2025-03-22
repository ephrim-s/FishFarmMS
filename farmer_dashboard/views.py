from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Pond, PondRental, Contract
from .serializers import PondSerializer, PondRentalSerializer, ContractSerializer


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

        rental = PondRental.obejcts.create(farmer=farmer, pond=pond, status='active')
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