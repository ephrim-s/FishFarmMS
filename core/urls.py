from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('order-history/', OrderHistoryView.as_view(), name='order_history'),
]