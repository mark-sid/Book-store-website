from django.db import models
from django.utils.text import slugify
from Authors.models import Author
from Bookstore.utils import get_upload_path


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
    author= models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books', null=True)
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



