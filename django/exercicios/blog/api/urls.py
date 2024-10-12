from django.urls import path
from . views import PostApiView, PostsApiView

urlpatterns = [
    path('a.post/', PostApiView.as_view(), name='a.post'),
    path('a.posts', PostsApiView.as_view(), name='a.posts')

]
