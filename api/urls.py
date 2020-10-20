from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FollowList, GroupList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="Posts")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="Comments"
)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/follow/", FollowList.as_view()),
    path("v1/group/", GroupList.as_view()),
    path(
        "v1/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "v1/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
