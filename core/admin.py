from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ADMIN_ROLES, USER_ROLES
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display in admin panel
    list_display = ('id', 'email', 'role', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff')
    ordering = ('email',)


    fieldsets = (
        ('Account Info', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image', 'geo_location', 'customer_address', 'destination_address')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define add_fieldsets for creating new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'role', 'phone_number', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    # Customize role field: Admins see all, others see limited choices
    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return super().get_fieldsets(request, obj) 
        return (
            ('Account Info', {'fields': ('email', 'password')}),
            ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image', 'geo_location', 'customer_address', 'destination_address')}),
        )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser and not request.user.is_staff:
            form.base_fields['role'].choices = USER_ROLES  # Limit role choices for non-admins
        return form

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = _("FishFarmMS Administration")
admin.site.site_title = _("FishFarmMS Admin Panel")
admin.site.index_title = _("Welcome to FishFarmMS Dashboard")
