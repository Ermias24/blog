from os import name
from django.urls import path
from .views import PostDetail, PostList, save_post


app_name = 'demoapp'


urlpatterns = [
    path('save-post/',save_post, name="save_post"),
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail')
    
]