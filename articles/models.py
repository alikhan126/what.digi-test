import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django_extensions.db import fields as extension_fields


def get_profile_image_upload_path(instance, filename):
    filename = f"{str(uuid.uuid4())[:8]}_{filename}"
    return os.path.join(f"blog/", filename)


class BaseTimeStampedModel(models.Model):
    """
    Abstract model that contains created_at, updated_at
    To be inherited by all other models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(BaseTimeStampedModel):
    title = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=get_profile_image_upload_path)
    tags = models.ManyToManyField(
        'articles.Tag', blank=True, related_name='article'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=(self.id,))


class Tag(BaseTimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
