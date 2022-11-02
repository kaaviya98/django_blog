from unicodedata import category
from django.shortcuts import render
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import HttpRequest,HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#   return render (request,'home.html',{})
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-updated"]
    # ordering=['-id']#ordering according to id


def CategoriesView(request, categories):
    category_post = Post.objects.filter(category=categories)
    return render(
        request,
        "categories.html",
        {"categories": categories, "category_post": category_post},
    )


# class AuthorsView(ListView):
#    model=Post
#    def get_queryset(self, *args, **kwargs):
#        return super().get_queryset(*args, **kwargs).filter(
#            author__username=self.kwargs['author']
#        )


class Blog_DetailView(DetailView):
    model = Post
    template_name = "blog_DetailView.html"


class Add_PostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # fields='__all__'---.since we use form control
    # fields=('title','body')#model fields name directly


class Add_CategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = ("name",)


class Update_PostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update_post.html"
    # fields=('title','body')
    # Post form is imported automatically by UpdateView


class Delete_PostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
