from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Account
from django.contrib.admin.views.decorators import staff_member_required


class AccountLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


@login_required
def login_success(request):
    if request.user.is_staff:
        return redirect("admin_dashboard")
    elif request.user.role == Account.Role.MENTOR:
        return redirect("mentor_dashboard")
    elif request.user.role == Account.Role.STUDENT:
        return redirect("student_dashboard")
    else:
        return redirect("login")

@staff_member_required(login_url="login")
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")