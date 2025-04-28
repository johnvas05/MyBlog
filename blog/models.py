from django.db import models
from django.conf import settings


class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'P', 'Published'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status, default=Status.DRAFT)

    class Meta:
        ordering = ['publish']

    def __str__(self):
        return self.title


