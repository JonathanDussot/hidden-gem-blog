"""
Database models for the Blog app.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Model representing the blog post section
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def total_likes(self):
        """
        Returns total amount of likes.
        """
        return self.likes.count()

    class Meta:
        """
        Orders in relation to creation date.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        returns name of post and its author.
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Model representing the comment section
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders in relation to creation date.
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        returns name of comment and its author.
        """
        return f"Comment {self.body} by {self.author}"