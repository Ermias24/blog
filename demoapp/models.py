from datetime import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    writer = models.CharField(max_length = 255, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(upload_to = "post_image/", blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


