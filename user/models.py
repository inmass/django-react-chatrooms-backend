from django.db import models
from django.utils.text import slugify

# Create your models here.

class Room(models.Model):
    users = models.ManyToManyField("auth.User", related_name="rooms", blank=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        count = 1
        while Room.objects.filter(slug=slug).exists():
            slug = slugify(f"{self.name}-{count}")
            count += 1

        self.slug = slug
        super().save(*args, **kwargs)