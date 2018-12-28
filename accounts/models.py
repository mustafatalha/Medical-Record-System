from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class MedUser(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'patient'),
      (3, 'nurse'),
      (4, 'relative')
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor')

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    creator = models.ForeignKey(MedUser, on_delete=models.CASCADE, related_name='patients')
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return self.user.username


class Nurse(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nurse')
    creator = models.ForeignKey(MedUser, on_delete=models.CASCADE, related_name='nurses')

    def __str__(self):
        return self.user.username


class Relative(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='relative')
    creator = models.ForeignKey(MedUser, on_delete=models.CASCADE, related_name='relatives')

    def __str__(self):
        return self.user.username


class Record(models.Model):
    patient = models.ForeignKey(MedUser, on_delete=models.CASCADE, related_name='record_patient')
    creator = models.ForeignKey(MedUser, on_delete=models.CASCADE, related_name='records')
    diagnostics = models.CharField(max_length=256, default='unknown', null=False, blank=False)
    allowed_users = models.ManyToManyField(MedUser,related_name='allowed_users') #TODO allowed records olarak değiştir
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return self.diagnostics