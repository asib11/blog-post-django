from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_time = models.DateTimeField(default=timezone.now)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    