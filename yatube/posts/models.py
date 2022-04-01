from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name='URL')
    description = models.TextField()

    def __str__(self):
        return self.title


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='group',
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        )
