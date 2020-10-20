from django.contrib import admin
from .models import Post, Comment, Follow, Group


admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
