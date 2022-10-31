from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.User_RegisterView.as_view(), name="register"),
]
