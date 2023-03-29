from django.urls import path
from .views import main, posts, subscriptions, logout_user, ticket_new, review_new, see_users, unfollow_user, delete_review


urlpatterns = [
    path("flux", main, name="reviews-main"),
    path("posts", posts, name="reviews-posts"),
    path("delete_review/<int:id_review>/", delete_review, name="review-delete"),
    path("subscriptions", see_users, name="reviews-subscriptions"),
    path("unfollow/<int:id_user>/", unfollow_user, name="unfollow_user"),
    path("logout", logout_user, name="reviews-logout"),
    path("new_ticket", ticket_new, name="reviews-new_ticket"),
    path("new_review", review_new, name="reviews-new_review"),
] 

