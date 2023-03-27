from django.urls import path
from .views import homepage_welcome, sign_up

urlpatterns = [
    path("", homepage_welcome, name="accounts_homepage"),
    path("sign_up", sign_up, name="accounts_sign_up"),
]