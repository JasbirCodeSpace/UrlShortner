from django.db import models

class ShortUrl(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(auto_now=True)
    total_hits = models.IntegerField(default=0)

    def __str__(self):
        return self.original_url