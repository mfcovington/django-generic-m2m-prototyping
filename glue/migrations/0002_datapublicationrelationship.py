# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('glue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPublicationRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data_object_id', models.PositiveIntegerField()),
                ('publication_object_id', models.PositiveIntegerField()),
                ('data_content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='related_data')),
                ('publication_content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='related_pubs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
