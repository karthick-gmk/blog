from django.db import models
from django.utils.text import slugify

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    image = models.ImageField(upload_to='posts/image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)


    def save(self, *args, **kwargs):
        if not self.slug:  # create slug only if it doesn’t exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField()


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


