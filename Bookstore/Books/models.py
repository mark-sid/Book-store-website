from django.db import models
from django.utils.text import slugify
import os
import uuid


# Create your models here.


def get_upload_path(filename):
    unique_id = uuid.uuid4()
    ext = filename.split('.')[-1]
    new_filename = f"{unique_id}.{ext}"
    return os.path.join('images/', new_filename)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=250)
    available = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    published_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.price}$'



