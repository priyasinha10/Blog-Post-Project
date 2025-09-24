from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
