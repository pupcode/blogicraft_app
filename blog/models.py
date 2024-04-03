from django.db import models
from django.db.models import ManyToManyField
from django.contrib.auth.models import User


# Create your models here.
class Announcement(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title  = models.CharField(max_length=100)
    teaser = models.TextField(default='The teaser text goes here')
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField(blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    image1 = models.ImageField( upload_to="images/", null= True, blank = True, max_length=None)
    image2 = models.ImageField( upload_to="images/", null= True, blank = True, max_length=None)
    tags = ManyToManyField(Tag)  # Many Posts can have Many Tags
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
