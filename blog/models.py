from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name="articles", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    likes = models.ManyToManyField(User, related_name="liked_articles", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="disliked_articles", blank=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="disliked_comments", blank=True
    )
