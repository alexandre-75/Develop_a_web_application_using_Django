from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Ticket
from django.contrib import messages
from .forms import NewTicketForm

def main(request):
    return render(request, "reviews/flux.html")

def posts(request):
    return render(request, "reviews/posts.html")

def subscriptions(request):
    return render(request, "reviews/subscriptions.html")

def logout_user(request):
    logout(request)
    return redirect("accounts_homepage")

def ticket_new(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST, request.FILES)

        if form.is_valid():
            print("hello")
            image = request.FILES.get('image', None)
            print("hella")
            Ticket.objects.create(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],
                image=image
            )
            messages.success(request, 'Your ticket has been posted!')
            return redirect('reviews-main')

    else:
        print("tata")
        form = NewTicketForm()

    context = {
        'form': form,
        'title': 'New Ticket'
    }

    return render(request, 'reviews/ticket_create.html', context)