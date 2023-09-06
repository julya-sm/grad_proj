from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('top/<slug:top_slug>/', BlogTopic.as_view(), name='top'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
]

