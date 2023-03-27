from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import login


def homepage_welcome(request):
    return render(request, "accounts/homepage.html")

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "accounts/sign_up.html", {"error": "mdp no correct"})
        user = CustomUser.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect("reviews-main")
        # return HttpResponse(f"bienvenue {username}")

    return render(request, "accounts/sign_up.html")
