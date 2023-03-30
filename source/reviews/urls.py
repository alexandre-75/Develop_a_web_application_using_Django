from django.urls import path
from .views import main, posts, subscriptions, logout_user, ticket_new, review_new, see_users, unfollow_user, delete_review, edit_review, delete_ticket, edit_ticket


urlpatterns = [
    path("flux", main, name="reviews-main"),
    path("new_ticket", ticket_new, name="reviews-new_ticket"),
    path("new_review", review_new, name="reviews-new_review"),

    path("posts", posts, name="reviews-posts"),
    path("delete_review/<int:id_review>/", delete_review, name="review-delete"),
    path("delete_ticket/<int:id_ticket>/", delete_ticket, name="ticket-delete"),
    path("edit_review/<int:id_review>/", edit_review, name="review-edit"),
    path("edit_ticket/<int:id_ticket>/", edit_ticket, name="ticket-edit"),

    path("subscriptions", see_users, name="reviews-subscriptions"),
    path("unfollow/<int:id_user>/", unfollow_user, name="unfollow_user"),

    path("logout", logout_user, name="reviews-logout"),
    
] 

