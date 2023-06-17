from django.db import models

from users.models import User

# Create your models here.
class Blog(models.Model):
    title       = models.CharField(max_length=255, default='', blank=False)
    content     = models.TextField()
    author      = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
