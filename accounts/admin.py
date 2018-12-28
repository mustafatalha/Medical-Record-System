from django.contrib import admin
from .models import Doctor, Patient, MedUser, Nurse, Relative, Record
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Relative)
admin.site.register(Record)
admin.site.register(MedUser, UserAdmin)