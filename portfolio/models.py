from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class HomeModel(models.Model):
    """Model definition for Home."""

    home_image = models.ImageField(default='default.png',
                                   upload_to='home_images/')
    head_text = models.TextField()
    home_desc = RichTextUploadingField(default='Enter Description here')

    class Meta:
        """Meta definition for HomeModel."""

        verbose_name = 'Home'
        verbose_name_plural = 'Home Data'

    def __str__(self):
        """Unicode representation of HomeModel."""
        return self.head_text
