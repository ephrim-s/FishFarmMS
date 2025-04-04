from rest_framework import serializers
from .models import Pond, PondRental, Contract, FishGrowth, Expense, Commission, CommissionRate, InsurancePackage, FarmerInsurance

class PondSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Pond
        fields = ['id', 'name', 'size', 'location', 'status']
    
    def get_size(self, obj):
        return obj.get_size()

class PondCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = fields = ['id', 'name', 'length', 'width', 'heigth', 'location', 'status', 'rental_price']
    
class PondRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondRental
        fields = ['id', 'farmer', 'pond', 'start_date', 'end_date', 'is_active']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class FishGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishGrowth
        fields = "__all__"
        read_only_fields = ['recorded_by']

class ExpenseSerializer(serializers.ModelSerializer):
    recorded_by = serializers.ReadOnlyField(source='recorded_by.email')
    farmer = serializers.ReadOnlyField(source='farmer.email')  

    class Meta:
        model = Expense
        fields = ['id', 'farmer', 'category', 'amount', 'description', 'date', 'recorded_by']
        
class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'type', 'amount', 'transaction', 'created_at']

class CommissionRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionRate
        fields = ['rental_rate', 'sales_rate', 'updated_at']
        read_only_fields = ['updated_at']

class InsurancePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePackage
        fields = '__all__'

class FarmerInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerInsurance
        fields = '__all__'