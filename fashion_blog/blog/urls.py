from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('top/<slug:top_slug>/', BlogTopic.as_view(), name='top'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
