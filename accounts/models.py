from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MedUser(User):
  USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'patient'),
      (3, 'nurse'),
      (4, 'relative')
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


class Doctor(models.Model):
    user = models.OneToOneField(MedUser, on_delete=models.CASCADE, related_name='doctor')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(MedUser, on_delete=models.CASCADE, related_name='patient')
    birth_date = models.BooleanField(blank=True)

    def __str__(self):
        return self.user.username
