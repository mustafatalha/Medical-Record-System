from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def doctor_login_required(view_func):
    doc_login_required = user_passes_test(lambda u: u.is_active and (u.user_type == 1),
                                          login_url='/accounts/login')
    decorated_view_func = login_required(doc_login_required(view_func), login_url='/accounts/login')
    return decorated_view_func


def patient_login_required(view_func):
    pat_login_required = user_passes_test(lambda u: u.is_active and (u.user_type == 2),
                                          login_url='/accounts/login')
    decorated_view_func = login_required(pat_login_required(view_func), login_url='/accounts/login')
    return decorated_view_func

def doctor_or_patient_login_required(view_func):
    doc_login_required = user_passes_test(lambda u: u.is_active and (u.user_type == 1 or u.user_type == 2 ),
                                          login_url='/accounts/login')
    decorated_view_func = login_required(doc_login_required(view_func), login_url='/accounts/login')
    return decorated_view_func