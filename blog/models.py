from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)

    @property
    def number_of_posts(self):
        if hasattr(self, "posts"):
            return self.posts.objects.count()
        return 0


class Tag(models.Model):
    name = models.CharField(max_length=24)


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish_at = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(Tag, blank=True)

    @property
    def is_published(self):
        return self.publish_at < timezone.now()

    def __str__(self):
        return f"Blog ({self.title[:16]}{'...' if len(self.title) > 16 else ''})"
