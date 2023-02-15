from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=30)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.user + ": " + self.message[:20]

