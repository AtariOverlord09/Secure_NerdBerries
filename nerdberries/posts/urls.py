from django.urls import path, re_path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('group/<slug:slug>/', views.category_posts, name='category_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    re_path(r'^get_image/(?P<filename>.+)/$', views.get_image, name='get_image'),
    path('create/', views.post_create, name='post_create'),
    path(
        'posts/<int:post_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path('follow/', views.follow_index, name='follow_index'),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
    path(
        'posts/<int:post_id>/make_purchase/',
        views.make_purchase, 
        name='make_purchase',
    ),
    path(
        'posts/<int:post_id>/return_purchase/',
        views.return_purchase, 
        name='return_purchase',
    ),
    path(
        'purchases/',
        views.purchases,
        name='purchases',
    ),
]