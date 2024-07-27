"""
Functions for the Blog app view code
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View, generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class LikeView(View):
    """
    Allows user to like or delete their like.
    """
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            messages.success(request, 'You unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You liked this post.')
        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))


class PostList(generic.ListView):
    """
    displays published blog posts
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    renders all post details on the page including likes and comments,
    and also allows user to comment on a post
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    total_likes = post.total_likes()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request,
                             'Comment submitted and awaiting approval.')
        else:
            messages.error(request,
                           'There was an error submitting your comment.')

    comment_form = CommentForm()

    return render(
        request,
        "blog/post-detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "total_likes": total_likes,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    """
    Allows user to edit thier comment
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment_form.save()
            messages.success(request, 'Comment updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return redirect('post-detail', slug=slug)


def comment_delete(request, slug, comment_id):
    """
    Allows users to delete their comment
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return redirect('post-detail', slug=slug)
