from os import name

from django.urls import path

from . import views

urlpatterns = [
    # define signup path
    path('accounts/signup/', views.signup, name="signup"),
    # defining user post routes
    path('', views.index, name="post_index"),
    # post by id we wont give a frontend for this actually we will but it's another story
    path('posts/<uuid:pk>', views.post_by_id, name="post_by_id"),
    # account profile
    path('accounts/profile/<str:username>', views.profile, name="profile")
]
