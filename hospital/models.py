from django.db import models
from django.contrib.auth.models import User
import uuid

#User._meta.get_field('email')._blank = False

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #email = models.EmailField(blank=False)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    name = models.CharField(max_length=100)
    appointment_date = models.DateField(null=True)
    diagnosis = models.CharField(max_length=100)
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    MILD = 'MD'
    MODERATE = 'ME'
    SEVERE = 'SE'
    SEVERITY_CHOICES = [
        (MILD, 'Mild'),
        (MODERATE, 'Moderate'),
        (SEVERE, 'Severe'),
    ]
    severity = models.CharField(
        max_length=2,
        choices=SEVERITY_CHOICES,
        default=MILD,
    )

    def __str__(self):
        return self.name