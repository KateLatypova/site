# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('visitor_hash', models.CharField(max_length=40, blank=True, db_index=True, null=True)),
                ('uri', models.CharField(max_length=255, blank=True, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, db_index=True, null=True)),
                ('last_visit', models.DateTimeField(blank=True, null=True)),
                ('visits', models.IntegerField(default=0)),
                ('object_app', models.CharField(max_length=255)),
                ('object_model', models.CharField(max_length=255)),
                ('object_id', models.CharField(max_length=255)),
                ('blocked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'visits',
                'verbose_name': 'visit',
                'ordering': ('uri', 'object_model', 'object_id'),
            },
        ),
    ]
