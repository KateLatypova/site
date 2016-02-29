# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentForImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', django_markdown.models.MarkdownField(verbose_name='comment text', max_length=256)),
                ('edits', django_markdown.models.MarkdownField(blank=True, verbose_name='old comments', max_length=4096)),
                ('created_at', models.DateTimeField(verbose_name='created at', editable=False, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(verbose_name='update at', default=django.utils.timezone.now)),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('imageObject', models.ForeignKey(to='gallery.AlbumImage', related_name='comments', verbose_name='image')),
            ],
            options={
                'verbose_name_plural': 'Comments for image',
                'verbose_name': 'Comment for image',
            },
        ),
    ]
