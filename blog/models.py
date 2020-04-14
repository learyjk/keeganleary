from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True)
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        """
        Set publish date to the date when post's published status is switched to True,
        reset the date if post is unpublished
        """
        if self.published and self.pub_date is None:
            self.pub_date = datetime.now()
        elif not self.published and self.pub_date is not None:
            self.pub_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
