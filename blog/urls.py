from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/new_post/', views.post_create, name='post_create'),
    path('blog/my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('<slug:slug>/edit/',views.post_edit, name='post_edit'),
    path('<slug:slug>/delete/',views.post_delete, name='post_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
    path('<slug:slug>/post_like', views.post_like, name='post_like'),
]