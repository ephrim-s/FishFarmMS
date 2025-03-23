from rest_framework import serializers
from .models import Pond, PondRental, Contract, FishGrowth, Expense

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = ['id', 'name', 'size', 'location', 'status']
    
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
        