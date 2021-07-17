from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=CASCADE, default=1)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"{self.title}"
