from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from reviews.models import Ticket
from django.contrib.auth import logout

def main(request):
    return render(request, "reviews/flux.html")

def posts(request):
    return render(request, "reviews/posts.html")

def subscriptions(request):
    return render(request, "reviews/subscriptions.html")

def logout_user(request):
    logout(request)
    return redirect("accounts_homepage")