from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Ticket, Review, UserFollows
from accounts.models import CustomUser
from .forms import NewTicketForm, NewReviewForm, SearchUserForm

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
        form = NewTicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],)
            return redirect('reviews-main')
    else:
        form = NewTicketForm()
    return render(request, 'reviews/ticket_create.html', context = {'form': form})

def review_new(request):
    if request.method == 'POST':
        t_form = NewTicketForm(request.POST)
        r_form = NewReviewForm(request.POST)

        if  r_form.is_valid():
            t = Ticket.objects.create(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],
            )
            t.save()
            Review.objects.create(
                ticket=t,
                user=request.user,
                headline=request.POST['headline'],
                rating=request.POST['rating'],
                body=request.POST['body']
            )
            return redirect('reviews-main')
    else:
        t_form = NewTicketForm()
        r_form = NewReviewForm()

    return render(request, 'reviews/review_create.html', context = {'t_form': t_form, 'r_form': r_form})
 
def see_users(request):

    users = CustomUser.objects.all().order_by("username")
    users_names = [user.username for user in users]

    relations = UserFollows.objects.filter(user=request.user)
    relations_users = [relation.followed_user.username for relation in relations]

    form = SearchUserForm()

    if request.method == "POST":

        form = SearchUserForm(request.POST)
        followed_name = request.POST["user_name"]
        if followed_name == request.user.username:
            context = {"users": users, "form": form, "relations": relations, "error": "id impossible"}
            return render(request, "reviews/subscriptions.html", context)

        if form.is_valid():
            new_relation = UserFollows()
            new_relation.user = request.user
            followed_user = CustomUser.objects.get(username=followed_name)
            new_relation.followed_user = followed_user
            new_relation.save()
            return redirect("reviews-subscriptions")

    context = {"users": users, "form": form, "relations": relations}
    return render(request, "reviews/subscriptions.html", context)

def unfollow_user(request, id_user):
    followed_user = get_object_or_404(CustomUser, id=id_user)
    relation = UserFollows.objects.filter(user=request.user, followed_user=followed_user)
    relation.delete()
    return redirect("reviews-subscriptions")
 