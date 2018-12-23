from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


rec_login_required = user_passes_test(lambda u: u.is_active and u.user_type == 1, login_url='/accounts/login')


def doctor_login_required(view_func):
    decorated_view_func = login_required(rec_login_required(view_func), login_url='/accounts/login')
    return decorated_view_func