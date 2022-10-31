from django.shortcuts import render
from .forms import PostForm

# from django.http import HttpRequest,HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#   return render (request,'home.html',{})
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-updated"]
    # ordering=['-id']#ordering according to id


class Blog_DetailView(DetailView):
    model = Post
    template_name = "blog_DetailView.html"


class Add_PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields='__all__'---.since we use form control
    # fields=('title','body')#model fields name directly


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
