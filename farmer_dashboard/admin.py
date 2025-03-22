from django.contrib import admin
from .models import Pond, PondRental, Contract, FishGrowth


@admin.register(Pond)
class PondAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'location', 'rental_price', 'status')
    search_fields = ('name', 'location')
    list_filter = ('status',)
    ordering = ('name',)


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