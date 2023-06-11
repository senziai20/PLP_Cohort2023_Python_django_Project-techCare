from django.db import models

# Create your models here.
# techcare_app/models.py

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Device(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    issue = models.TextField()

    def __str__(self):
        return self.name


class RepairRequest(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default='PENDING')

    def __str__(self):
        return f"Repair request for {self.device.name}"
