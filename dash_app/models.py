from django.db import models

class Ride(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )

    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    distance = models.FloatField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride - {self.pk}"
