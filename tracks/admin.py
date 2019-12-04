from django.contrib import admin
from .models import Tracks, Like


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'track')


admin.site.register(Like, LikeAdmin)
admin.site.register(Tracks, TrackAdmin)
