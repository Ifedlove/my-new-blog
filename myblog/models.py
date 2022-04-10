

from cgitb import text
from django.conf import settings
from django.db import models
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    

    def __str__(self):
        return self.title

# Create your models here.
