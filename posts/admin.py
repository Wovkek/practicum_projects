from django.contrib import admin
from .models import Comment, Post, Group, Follow


class PostAdmin(admin.ModelAdmin):
     list_display = ('pk', 'text', 'pub_date', 'author',)
     search_fields = ('text',)
     list_filter = ('pub_date',)
     empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
     list_display = ('pk', 'title', 'slug', 'description',)
     search_fields = ('title',)
     list_filter = ('slug',)
     empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
     list_display = ('pk', 'text', 'author', 'created', 'post',)
     search_fields = ('pk', 'text',)
     list_filter = ('created',)
     empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
     list_display = ('author', 'user',)
     search_fields = ('author', 'user',)
     list_filter = ('author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
