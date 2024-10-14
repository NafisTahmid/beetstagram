from django.contrib import admin
from django.urls import path
from App_Login import views


app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('profile/', views.profile, name="profile"),
    path('user/<username>/', views.user, name="user"),
    path('follow/<username>/', views.follow, name="follow"),
    path('unfollow/<username>/', views.unfollow, name="unfollow"),
    path('change_password/', views.change_password, name="change_password")

]


