# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('settings', models.TextField(default='{}')),
                ('object_id', uuidfield.fields.UUIDField(max_length=32, null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='usersettings',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
        # PostgreSQL does not consider null values for unique constraints;
        # UserSettings for Users have no content_object; the following ensures
        # there can only be one such entry per user
        migrations.RunSQL(
            'CREATE UNIQUE INDEX usersettings_unique_null ON usersettings_usersettings (user_id) WHERE content_type_id IS NULL;',
            'DROP INDEX usersettings_unique_null;'
        )
    ]
