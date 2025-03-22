from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Add password2 field

    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'phone_number', 'profile_image', 'geo_location', 
                  'customer_address', 'destination_address', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 before creating the user
        return User.objects.create_user(**validated_data)

# Customized JWT Token to include user role
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token