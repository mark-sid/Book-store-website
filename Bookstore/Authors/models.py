from django.db import models
from Bookstore.utils import get_upload_path
from django.utils.text import slugify


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)
    portrait = models.ImageField(upload_to=get_upload_path, null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    bio = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name