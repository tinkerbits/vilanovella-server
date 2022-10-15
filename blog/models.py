from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    preheader = models.TextField()
    post_image_1 = models.ImageField(blank=True, null=True)
    post_image_2 = models.ImageField(blank=True, null=True)
    post_image_3 = models.ImageField(blank=True, null=True)
    post_image_4 = models.ImageField(blank=True, null=True)
    post_image_5 = models.ImageField(blank=True, null=True)
    post_image_6 = models.ImageField(blank=True, null=True)
    post_image_7 = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        commentstring = self.comment[0:100]+"..."
        return f'{self.name}: "{commentstring}" [{(self.last_modified).strftime("%H:%M:%S, %d %b %Y")}]'
