from django.contrib import admin
from .models import Pond, PondRental, Contract, FishGrowth, CommissionRate, Commission, Expense


@admin.register(Pond)
class PondAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'formatted_size', 'location', 'rental_price', 'status')
    search_fields = ('name', 'location')
    list_filter = ('status',)
    ordering = ('name',)

    def formatted_size(self, obj):
        return obj.get_size()
    
    formatted_size.short_description = 'Size (L x W x H)'


@admin.register(PondRental)
class PondRentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmer', 'pond', 'start_date', 'end_date', 'is_active')
    search_fields = ('farmer__email', 'pond__name')
    list_filter = ('is_active', 'start_date', 'end_date')
    ordering = ('-start_date',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental', 'contract_file', 'created_at')
    search_fields = ('rental__pond__name', 'rental__farmer__email')
    ordering = ('-created_at',)

@admin.register(FishGrowth)
class FishGrowthAdmin(admin.ModelAdmin):
    list_display = ("rental", "recorded_at", "size_in_cm")
    list_filter = ("recorded_at",)
    search_fields = ("rental__pond__name", "rental__farmer__email")

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'farmer', 'category', 'amount', 'description', 'date', 'recorded_by_name')
    search_fields = ('category', 'description', 'farmer__email', 'recorded_by_name')
    list_filter = ('category', 'date')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.is_staff:  
            return qs  
        return qs.filter(farmer=request.user)

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['type', 'amount', 'transaction', 'created_at']
    list_filter = ['type', 'created_at']

@admin.register(CommissionRate)
class CommissionRateAdmin(admin.ModelAdmin):
    list_display = ['rental_rate', 'sales_rate', 'updated_at']