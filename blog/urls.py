"""
URL paths to render each view to the browser.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit-comment/<int:comment_id>/', views.comment_edit,
         name='comment_edit'),
    path('<slug:slug>/delete-comment/<int:comment_id>/', views.comment_delete,
         name='comment_delete'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like_post'),
]
