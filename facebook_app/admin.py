from django.contrib import admin
from .models import *


class PostContentInline(admin.TabularInline):
    model = PostContent
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostContentInline]

class CommentInline(admin.TabularInline):
    model = CommentLike
    extra = 0

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 1

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    inlines = [FavoriteItemInline]

admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(Hashtag)
admin.site.register(Location)