from django.urls import path
from .views import main, posts, subscriptions, logout_user


urlpatterns = [
    path("flux", main, name="reviews-main"),
    path("posts", posts, name="reviews-posts"),
    path("subscriptions", subscriptions, name="reviews-subscriptions"),
    path("logout", logout_user, name="reviews-logout"),
] 

