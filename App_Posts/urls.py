from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from App_Posts import views
app_name = 'App_Posts'
urlpatterns = [
    path('', views.home, name="home"),
    path('like/<pk>', views.liked, name="like"),
    path('unlike/<pk>', views.unliked, name="unlike"),
    path('post_details/<pk>', views.post_details, name='post_details'),
    path('edit_post/<pk>', views.edit_post, name='edit_post'),
    path('delete_post/<pk>', views.delete_post, name="delete_post")
]
