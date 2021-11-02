from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    body = models.CharField(max_length=144)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')


