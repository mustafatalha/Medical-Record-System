from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/buyer', register_doctor, name= 'register_doctor'),
    path('register/seller', register_patient, name= 'register_patient'),
    path('logout/', logout, name= 'logout'),
    path('profile/', profile, name= 'profile'),
    path('', get_home, name = 'home'),
]