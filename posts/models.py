from django.db import models
from django.urls import reverse

class Post(models.Model):
    user = models.CharField(max_length=30)
    message = models.TextField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ": " + self.message[:20]
    
    def get_absolute_url(self):
        return reverse("home")