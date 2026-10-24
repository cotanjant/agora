from django.utils import timezone
from tokenize import blank_re
from uuid import uuid4
from django.db import models

from django.contrib.auth.models import User
import uuid

# Table will be like:
# title | content | published | published_at | publisher

class Post(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    title = models.CharField(
        max_length=255,
        blank=False,
    )
    content = models.TextField(
        blank=False,
    )
    published = models.BooleanField()
    published_at = models.DateTimeField(
        default=timezone.now
    )
    publisher = models.ForeignKey(
        User,
        # this line will delete user's all posts if user deletes it's profile
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title
