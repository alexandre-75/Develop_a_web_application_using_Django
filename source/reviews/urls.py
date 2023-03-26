
from django.urls import path
from .views import main, index, product_detail, logout_user


urlpatterns = [
    path("", main, name="reviews-main"),
    path("posts", index, name="reviews-posts"),
    path("subscriptions", main, name="reviews-subscriptions"),
    path("logout", logout_user, name="reviews-logout"),
    path("<str:slug>", product_detail, name="product")
] 

