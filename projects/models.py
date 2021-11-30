from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    slug = models.SlugField(default="", blank= True, editable=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("project-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

