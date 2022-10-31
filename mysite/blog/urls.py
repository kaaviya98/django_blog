from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home')
    path("", views.HomeView.as_view(), name="home"),
    path(
        "blog_detail/<int:pk>",
        views.Blog_DetailView.as_view(),
        name="blog_detail",
    ),
]
