from django.db import models

# Create your models here.
from django.conf import settings

class CustomUser(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20, unique=True)
    personal_number_designation = models.CharField(max_length=20, unique=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.surname} ({self.username})"

class LeaveApplication(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Annual', 'Annual Leave'),
        ('Sick', 'Sick Leave'),
        ('Maternity', 'Maternity Leave'),
        ('Paternity', 'Paternity Leave'),
        ('Compassionate', 'Compassionate Leave'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)  # New field
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    manager_comments = models.TextField(null=True, blank=True)  # Manager's approval/rejection reason
    applied_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def leave_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"LeaveApplication({self.user}, {self.leave_type}, {self.status})"

class LeaveBalance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_days = models.IntegerField(default=15)
    used_days = models.IntegerField(default=0)

    @property
    def remaining_days(self):
        return self.total_days - self.used_days

    def __str__(self):
        return f"LeaveBalance({self.user}, Remaining: {self.remaining_days})"
