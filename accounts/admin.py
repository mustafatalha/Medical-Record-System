from django.contrib import admin
from .models import Doctor, Patient, MedUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MedUser,UserAdmin)