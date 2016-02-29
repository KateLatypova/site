from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django_markdown.models import MarkdownField


class AlbumImage(models.Model):
    name = models.CharField(verbose_name='name', max_length=128)
    image = models.ImageField(verbose_name='image', upload_to='gallery')

    class Meta:
        verbose_name = 'Album image'
        verbose_name_plural = 'Album images'


class CommentForImage(models.Model):
    imageObject = models.ForeignKey('AlbumImage', verbose_name='image', related_name='comments')
    author = models.ForeignKey(User, verbose_name='author')
    text = MarkdownField(verbose_name='comment text', max_length=256)
    edits = MarkdownField(verbose_name='old comments', max_length=4096, blank=True)
    created_at = models.DateTimeField(verbose_name='created at', default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name='update at', default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment for image'
        verbose_name_plural = 'Comments for image'