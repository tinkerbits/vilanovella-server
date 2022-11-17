from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    hero_image = models.URLField(blank=True, null=True)
    preheader = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        commentstring = self.comment[0:100]+"..."
        return f'{self.name}: "{commentstring}" [{(self.last_modified).strftime("%H:%M:%S, %d %b %Y")}]'
