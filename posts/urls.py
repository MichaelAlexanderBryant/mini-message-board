from django.urls import path

from .views import PostListView, PostCreateView

urlpatterns = [
    path("new/", PostCreateView.as_view(), name="new_message"),
    path("", PostListView.as_view(), name="home")
]