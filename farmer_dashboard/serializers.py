from rest_framework import serializers
from .models import Pond, PondRental, Contract, FishGrowth, Expense, Commission, CommissionRate, InsurancePackage, FarmerInsurance

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = ['id', 'name', 'location', 'status']
    
    # def get_size(self, obj):
    #     return obj.get_size()
    
class PondRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondRental
        fields = ['id', 'farmers', 'pond', 'rental_start', 'rental_end', 'status']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class FishGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishGrowth
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    recorded_by = serializers.ReadOnlyField(source='recorded_by.email')

    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description', 'date', 'recorded_by']

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'type', 'amount', 'transaction', 'created_at']

class CommissionRateSerializer(serializers.ModelField):
    class Meta:
        model = CommissionRate
        fields = ['rental-rate', 'sales_rate', 'updated_at']
        read_only_fields = ['updated_at']

class InsurancePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePackage
        fields = '__all__'

class FarmerInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerInsurance
        fields = '__all__'