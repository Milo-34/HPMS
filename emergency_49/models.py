from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)

    def clean(self):
        if self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason_for_visit = models.TextField()

    def __str__(self):
        return f"Appointment of {self.patient} with {self.doctor} on {self.appointment_date}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Record for {self.patient} on {self.record_date}"

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bills')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.patient} - Amount Due: {self.amount_due} ({'Paid' if self.is_paid else 'Unpaid'})"

