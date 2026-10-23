from django.urls import path

from . import views

urlpatterns = [
    # define signup path
    path('accounts/signup/', views.signup, name="signup")
]
