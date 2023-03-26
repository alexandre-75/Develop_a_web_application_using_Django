from django.urls import path
from django.contrib.auth import views as auth_views
from .views import homepage_welcome, sign_up

urlpatterns = [
    path("", homepage_welcome, name="accounts_homepage"),
    path("sign_up", sign_up, name="accounts_sign_up"),
]