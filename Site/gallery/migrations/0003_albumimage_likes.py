# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_commentforimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumimage',
            name='likes',
            field=models.ManyToManyField(related_name='likes_images', blank=True, verbose_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
