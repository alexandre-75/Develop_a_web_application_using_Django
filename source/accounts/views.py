from django.shortcuts import render


def homepage_welcome(request):
    return render(request, "accounts/homepage.html")

def sign_up(request):
    return render(request, "accounts/sign_up.html")
