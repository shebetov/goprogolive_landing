from django.shortcuts import render, redirect
from .models import SiteEmailLog


# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            SiteEmailLog.objects.create(
                email=str(request.POST["email"]),
                ip_addr=str(request.META['HTTP_X_REAL_IP']),
                user_agent=str(request.META['HTTP_USER_AGENT'])
            )
        except Exception as e:
            print("Exception: " + str(e))
            SiteEmailLog.objects.create(
                email=str(request.POST["email"]),
                ip_addr="127.0.0.1",
                user_agent="error"
            )
        return redirect(success)
    return render(request, "index.html")


def redirect_to_index(request):
    return redirect("/")


def success(request):
    return render(request, "success.html")
