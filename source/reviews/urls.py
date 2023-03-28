from django.urls import path
from .views import main, posts, subscriptions, logout_user, ticket_new, review_new, see_users


urlpatterns = [
    path("flux", main, name="reviews-main"),
    path("posts", posts, name="reviews-posts"),
    path("subscriptions", see_users, name="reviews-subscriptions"),
    path("logout", logout_user, name="reviews-logout"),
    path("new_ticket", ticket_new, name="reviews-new_ticket"),
    path("new_review", review_new, name="reviews-new_review"),
] 

