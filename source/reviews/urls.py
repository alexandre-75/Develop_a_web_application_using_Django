
from django.urls import path
from .views import main, index, product_detail


urlpatterns = [
    path("", main, name="reviews-main"),
    path("posts", main, name="reviews-posts"),
    path("subscriptions", main, name="reviews-subscriptions"),
    path("logout", index, name="reviews-logout"),
    path("<str:slug>", product_detail, name="product")
] 
