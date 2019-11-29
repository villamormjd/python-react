from django.contrib import admin
from .models import Tracks


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Tracks, TrackAdmin)
