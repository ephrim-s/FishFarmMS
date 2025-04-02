from rest_framework.permissions import BasePermission, SAFE_METHODS


# This permission allows access to only users with admin role
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


# This permission allows access to only users with Admin or Worker role
class IsWorkerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_athenticated and request.user.role in ["worker", "admin"]
    

# This permission allows access to only users with External Farmers role
class IsExternalFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'farmer'

# This permission allows access to only users with Outgrower Farmers role
class IsOutgrowerFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'outgrower'

# This permission allows access to only users with wholesale, retail and consumer
class IsWholesalerOrRetailerOrConsumer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['wholesaler', 'retailer', 'consumer']
