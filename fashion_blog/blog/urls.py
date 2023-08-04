from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]

