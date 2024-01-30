from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/new_post/', views.post_create, name='post_create'),
    path('<slug:slug>/edit/',views.post_edit, name='post_edit'),
    path('<slug:slug>/delete/',views.post_delete, name='post_delete'),
]