from django.db import models
from django_extensions.db.models import TimeStampedModel


class Publisher(TimeStampedModel):
    domain = models.CharField(max_length=255, unique=True)
    pc1 = models.FloatField()

    def __str__(self):
        return self.domain

class Article(TimeStampedModel):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    url = models.URLField(max_length=1000, unique=True)
    description = models.TextField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, related_name="articles", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    published_at = models.DateTimeField()
    author = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
