from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('blog_detail',args=(str(self.id)))
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('blog_detail',args=(str(self.id)))
        return reverse(
            "home",
        )
