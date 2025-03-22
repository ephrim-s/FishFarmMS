from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Pond(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance')
    ]

    name = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=20, decimal_places=2) # Size in squre ft
    location = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"

class PondRental(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pond_rentals')
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE, related_name='rentals')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            self.pond.status = 'rented'
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
