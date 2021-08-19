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


class AboutModel(models.Model):
    """
    Model definition for AboutModel.
    
    ? Purpose:
        ! Define Data to be shown at About Page
    ? What Data?
        ! Information on why this Project Exist and contributers etc
    """

    about_head_image = models.ImageField(upload_to='about_images/')
    about_head_text = models.CharField(max_length=100, blank=False)
    about_head_sub_text = models.TextField(blank=False)
    about_page_desc = RichTextUploadingField(
        default='Enter Description on what the Page is about')

    class Meta:
        """Meta definition for AboutModel."""

        verbose_name = 'About Page'
        verbose_name_plural = 'About Page Data'

    def __str__(self):
        """Unicode representation of AboutModel."""
        return self.about_head_text
