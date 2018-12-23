from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm, DoctorRegistrationForm, PatientRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .decorators import doctor_login_required
# Create your views here.


def get_home(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username_or_email']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Can't login now.")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def register_doctor(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        doctor_form = DoctorRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 1
            user.is_active = False
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()

            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']

            return redirect("/")
    else:
        user_form = UserRegistrationForm()
        doctor_form = DoctorRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': doctor_form})


@doctor_login_required
def register_patient(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        patient_form = PatientRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            user.user_type = 2
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()

            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']

            return redirect("/")
    else:
        user_form = UserRegistrationForm()
        patient_form = PatientRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': patient_form})


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url="/accounts/login")
def profile(request):
    return render(request, "accounts/profile.html")