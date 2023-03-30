from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Ticket, Review, UserFollows
from accounts.models import CustomUser
from .forms import NewTicketForm, NewReviewForm, SearchUserForm

def main(request):

    list_review_personal = []
    ticket_no_comment = []
    review_final = []
    ticket_final = []

    list_review_ticket_id = []
    list_id_followed_users = []
    list_id_review_followed_user = []
    list_id_ticket_followed_user = []
    
    listfinal = []

    followed_user = UserFollows.objects.filter(user=request.user)
    review = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)

    for i in review:
        list_review_personal.append(i)
        listfinal.append(i)

    for i in range(len(review)):
        a = review[i].ticket_id
        list_review_ticket_id.append(a)

    for tick in tickets:
        if tick.id not in list_review_ticket_id:
            ticket_no_comment.append(tick)
            listfinal.append(tick)
    
    for i in followed_user:
        list_id_followed_users.append(i.followed_user_id)

    review_all_user = Review.objects.all()
    for i in review_all_user:
        if i.user_id in list_id_followed_users:
            list_id_review_followed_user.append(i.id)
    
    for i in list_id_review_followed_user:
        reviews = Review.objects.filter(id__in=[i])
        for z in reviews:
            review_final.append(z)
            listfinal.append(z)

    ticket_all_user = Ticket.objects.all()
    for i in ticket_all_user:
        if i.user_id in list_id_followed_users:
            list_id_ticket_followed_user.append(i.id)
        
    for i in list_id_ticket_followed_user:
        tickets = Ticket.objects.filter(id__in=[i])
        for z in tickets:
            ticket_final.append(z)
            listfinal.append(z)

    sorted_listfinal = sorted(listfinal, key=lambda post: post.time_created, reverse=True)

    context={"f": review_final, "ff": ticket_final, "r":list_review_personal, "rr":ticket_no_comment,  "ss": sorted_listfinal}
    return render(request, "reviews/flux.html", context)

def posts(request):

    list_review_ticket_id =[]
    ticket_no_comment = []

    review = Review.objects.filter(user=request.user)

    for i in range(len(review)):
        a = review[i].ticket_id
        list_review_ticket_id.append(a)

    tickets = Ticket.objects.filter(user=request.user)

    for tick in tickets:
        if tick.id not in list_review_ticket_id:
            ticket_no_comment.append(tick)


    return render(request, "reviews/posts.html", context ={"review":review, "ticket":ticket_no_comment}) 

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

    r = UserFollows.objects.filter(followed_user=request.user)
    r_users = [relation.user.username for relation in r]

    form = SearchUserForm()

    if request.method == "POST":

        form = SearchUserForm(request.POST)
        followed_name = request.POST["user_name"]
        if followed_name == request.user.username:
            context = {"users": users, "form": form, "relations": relations, "error": "id impossible", "r_users": r,}
            return render(request, "reviews/subscriptions.html", context)

        if form.is_valid():
            new_relation = UserFollows()
            new_relation.user = request.user
            followed_user = CustomUser.objects.get(username=followed_name)
            new_relation.followed_user = followed_user
            new_relation.save()
            return redirect("reviews-subscriptions")

    context = {"users": users, "form": form, "relations": relations, "r_users": r,}
    return render(request, "reviews/subscriptions.html", context)

def unfollow_user(request, id_user):
    followed_user = get_object_or_404(CustomUser, id=id_user)
    relation = UserFollows.objects.filter(user=request.user, followed_user=followed_user)
    relation.delete()
    return redirect("reviews-subscriptions")

def delete_review(request, id_review):
    revw = Review.objects.filter(user=request.user, id = id_review)
    revw.delete()
    return redirect("reviews-posts")

def edit_review(request, id_review):

    instance = get_object_or_404(Review, id=id_review)
    review = Review.objects.filter(id=id_review)

    if request.method == "POST":
        form = NewReviewForm(request.POST, instance=instance)
        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.user = request.user
            edited_review.save()
            return redirect("reviews-posts")
    else:
        form = NewReviewForm(instance=instance)

    return render(request, "reviews/edit_review.html", {"form": form, "review": review})

def delete_ticket(request, id_ticket):
    tikt = Ticket.objects.filter(user=request.user, id = id_ticket)
    tikt.delete()
    return redirect("reviews-posts")

def edit_ticket(request, id_ticket):

    instance = get_object_or_404(Ticket, id=id_ticket)

    if request.method == "POST":
        form = NewTicketForm(request.POST, instance=instance)
        if form.is_valid():
            edited_ticket = form.save(commit=False)
            edited_ticket.user = request.user
            edited_ticket.save()
            return redirect("reviews-posts")
    else:
        form = NewTicketForm(instance=instance)
    return render(request, "reviews/edit_ticket.html", {"form": form})