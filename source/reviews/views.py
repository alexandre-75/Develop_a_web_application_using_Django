from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from reviews.models import Ticket
from django.contrib.auth import logout

def main(request):
    return render(request, "reviews/index.html")

def index(request):
    tickets = Ticket.objects.all()
    return render(request, "reviews/index.html", context = {"tickets": tickets})

def product_detail(request, slug):
    product = get_object_or_404(Ticket, slug=slug)
    return HttpResponse(product.description)

def logout_user(request):
    logout(request)
    return redirect("accounts_homepage")