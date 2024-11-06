from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment