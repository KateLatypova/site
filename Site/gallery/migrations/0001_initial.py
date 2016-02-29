# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=128)),
                ('image', models.ImageField(verbose_name='image', upload_to='gallery')),
            ],
            options={
                'verbose_name': 'Album image',
                'verbose_name_plural': 'Album images',
            },
        ),
    ]
