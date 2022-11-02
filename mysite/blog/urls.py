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
    path("add_post/", views.Add_PostView.as_view(), name="add_post"),
    path(
        "add_category/", views.Add_CategoryView.as_view(), name="add_category"
    ),
    path(
        "blog_detail/edit/<int:pk>",
        views.Update_PostView.as_view(),
        name="blog_detail_edit",
    ),
    path(
        "blog_detail/<int:pk>/delete",
        views.Delete_PostView.as_view(),
        name="blog_detail_delete",
    ),
    path(
        "categories/<str:categories>", views.CategoriesView, name="categories"
    ),
    # path('authors/<str:author>/<int:pk>',views.AuthorsView.as_view(),name="authors"),
]
