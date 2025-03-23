from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from . permissions import *

User = get_user_model()

# This is an API for User Registration
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

# This is a Custom JWT Login API
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome, Admin"})
    
class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated, IsWholesalerOrRetailerOrConsumer]

    def get(self, request):
        return Response({"message": "Order history for Wholesalers, Retailers, and Consumers!"})