from django.contrib.auth import get_user_model
from django.db import models
from decimal import Decimal

User = get_user_model()

class Pond(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance')
    ]

    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=20, decimal_places=0) 
    width = models.DecimalField(max_digits=20, decimal_places=0)
    heigth = models.DecimalField(max_digits=20, decimal_places=1) 
    location = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
    
    def get_size(self):
        return f"{self.length} x {self.width} x {self.heigth} ft"

class PondRental(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pond_rentals')
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE, related_name='rentals')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            self.pond.status = 'rented'
        else:
            self.pond.status = 'available'

        self.pond.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.farmer.email} rented {self.pond.name} from {self.start_date} to {self.end_date}"
    
class Contract(models.Model):
    rental = models.OneToOneField(PondRental, on_delete=models.CASCADE, related_name='contract')
    contract_file = models.FileField(upload_to='contracts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract for {self.rental.pond.name} rented by {self.rental.farmer.email}"

class FishGrowth(models.Model):
    rental = models.ForeignKey(PondRental, on_delete=models.CASCADE, related_name='growth_records')
    image = models.ImageField(upload_to="fish_growth/images/", blank=True, null=True)
    video = models.FileField(upload_to="fish_growth/videos/", blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    size_in_cm = models.DecimalField(max_digits=5, decimal_places=2, help_text="Fish size in cm")

    def __str__(self):
        return f"Growht record for {self.rental.pond.name} on {self.recorded_at}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('feed', 'Feed'),
        ('medication', 'Medication'),
        ('maintenance', 'Maintenance'),
        ('fingerlings', 'Fingerlings'),
        ('others', 'Others'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recorded_by_name = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.recorded_by and not self.recorded_by_name:
            self.recorded_by_name = self.recorded_by.get_full_name() or self.recorded_by.email
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_cagetory_display()} - {self.amount}"
    
    
class CommissionRate(models.Model):
    rental_rate = models.DecimalField(max_digits=5, decimal_places=2, default=10.00, help_text="Commission percentage for pond rentals")
    sales_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00,   help_text="Commission percentage for fish sales"  )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rental: {self.rental_rate}%, Sales: {self.sales_rate}%"

    @classmethod
    def get_current_rates(cls):
        """Retrieve the latest commission rates (or create default if none exist)."""
        obj, _ = cls.objects.get_or_create(id=1)  # Ensures a single instance exists
        return obj
    
    
class Commission(models.Model):
    COMMISSION_TYPES = [
        ('rental', 'Pond Rental'),
        ('sales', 'Fish Sales'),
    ]
    type = models.CharField(max_length=20, choices=COMMISSION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.CharField(max_length=100, help_text="Related transactoin ID or reference")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} commission of GHs{self.amount} on {self.transaction}"
    
    @staticmethod
    def calculate_pond_rental_commission(rental):
        rates = CommissionRate.get_current_rates()
        commission_rate = Decimal(rates.rental_rate) / 100
        commission_amount = rental.pond.rental_price * commission_rate
        return Commission.objects.create(
            type='rental',
            amount=commission_amount,
            transaction=f"Rental-{rental.id}"
        )

class InsurancePackage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_details = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

class FarmerInsurance(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insurance_policies')
    insurance_package = models.ForeignKey(InsurancePackage, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Ensure only one active policy per farmer
        if self.is_active:
            FarmerInsurance.objects.filter(farmer=self.farmer, is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.farmer.email} - {self.insurance_package.name} ({'Active' if self.is_active else 'Expired'})"