from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import (UserLoginForm, UserRegistrationForm1, UserRegistrationForm2, DoctorRegistrationForm,
                    PatientRegistrationForm, NurseRegistrationForm, RelativeRegistrationForm, RecordCreationForm)
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import BaseUserManager

from .decorators import doctor_login_required, patient_login_required
from .models import MedUser,Patient
# Create your views here.


def get_home(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Login information is wrong or your account is not active.")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def register_doctor(request):
    if request.method == "POST":
        user_form = UserRegistrationForm1(request.POST)
        doctor_form = DoctorRegistrationForm(request.POST)


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
            user = authenticate(username=u, password=p)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Registration completed, Please contact with site admin for activation.")
    else:
        user_form = UserRegistrationForm1()
        doctor_form = DoctorRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': doctor_form})


@doctor_login_required
def register_patient(request):
    if request.method == "POST":
        user_form = UserRegistrationForm2(request.POST)
        patient_form = PatientRegistrationForm(request.POST)

        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 2
            user.username = user.first_name[0] + user.last_name
            pwd = BaseUserManager().make_random_password()
            user.set_password(pwd)
            user.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.creator = MedUser.objects.get(username = request.user)
            patient.save()

            user_form.add_error(None, "Patient registered with username = {} with random password = {}"
                                .format(user.username,pwd))
            # return redirect("/")
    else:
        user_form = UserRegistrationForm2()
        patient_form = PatientRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': patient_form})


@doctor_login_required
def register_nurse(request):
    if request.method == "POST":
        user_form = UserRegistrationForm2(request.POST)
        nurse_form = NurseRegistrationForm(request.POST)

        if user_form.is_valid() and nurse_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 3
            user.username = user.first_name[0] + user.last_name
            pwd = BaseUserManager().make_random_password()
            user.set_password(pwd)
            user.save()
            nurse = nurse_form.save(commit=False)
            nurse.user = user
            nurse.creator = MedUser.objects.get(username = request.user)
            nurse.save()

            user_form.add_error(None, "Nurse registered with username = {} with random password = {}"
                                .format(user.username,pwd))
            # return redirect("/")
    else:
        user_form = UserRegistrationForm2()
        nurse_form = NurseRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': nurse_form})


@patient_login_required
def register_relative(request):
    if request.method == "POST":
        user_form = UserRegistrationForm2(request.POST)
        relative_form = RelativeRegistrationForm(request.POST)

        if user_form.is_valid() and relative_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 4
            user.username = user.first_name[0] + user.last_name
            pwd = BaseUserManager().make_random_password()
            user.set_password(pwd)
            user.save()
            relative = relative_form.save(commit=False)
            relative.user = user
            relative.creator = MedUser.objects.get(username = request.user)
            relative.save()

            user_form.add_error(None, "Relative registered with username = {} with random password = {}"
                                .format(user.username,pwd))
            # return redirect("/")
    else:
        user_form = UserRegistrationForm2()
        relative_form = NurseRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': relative_form})


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url="/accounts/login")
def profile(request):
    return render(request, "accounts/profile.html")


@doctor_login_required
def create_record(request):
    if request.method == 'POST':
        record_form = RecordCreationForm(request.POST)

        if record_form.is_valid():
            record = record_form.save(commit=False)
            pat = MedUser.objects.get(username=record_form.cleaned_data['patient_username'])
            record.patient = pat
            record.first_name = pat.first_name
            record.last_name = pat.last_name
            record.birth_date = Patient.objects.get(user=pat).birth_date
            record.creator = MedUser.objects.get(username=request.user)
            record.save()
            record.allowed_users.add(pat)
            record.allowed_users.add(MedUser.objects.get(username=request.user))
            record.save()

            return redirect("/") # TODO Burada record detay sayfasına yönlendirme olacak
    else:
        record_form = RecordCreationForm(request.POST)

    return render(request, "accounts/create_record.html", {'record_form': record_form})


@login_required()
def allowed_records(request):
    return render(request,"accounts/records.html")