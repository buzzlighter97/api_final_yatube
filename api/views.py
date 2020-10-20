from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    PostSerializer,
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
)
from .models import Post, Comment, Follow, Group
from rest_framework.generics import (
    ListCreateAPIView,
)
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status, filters
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "group",
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        post = get_object_or_404(Post, id=post_id)
        comments_queryset = post.comments
        return comments_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowList(ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["=following__username", "=user__username"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupList(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
