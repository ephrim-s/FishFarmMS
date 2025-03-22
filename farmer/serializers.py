from rest_framework import serializers
from .models import Pond, PondRental, Contract

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = ['id', 'name', 'size', 'location', 'is_available']
    
class PondRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondRental
        fields = ['id', 'farmers', 'pond', 'rental_start', 'rental_end', 'status']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
