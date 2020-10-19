from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FollowList, GroupList

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="Posts")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="Comments"
)

urlpatterns = [
    path("", include(v1_router.urls)),
    path("follow/", FollowList.as_view()),
    path("group/", GroupList.as_view())
]
