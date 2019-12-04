from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class Tracks(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField()  # charfield with some addtional url validation
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey('tracks.Tracks', related_name='likes', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user