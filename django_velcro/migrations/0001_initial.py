# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPublicationsRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data_object_id', models.PositiveIntegerField()),
                ('publications_object_id', models.PositiveIntegerField()),
                ('data_content_type', models.ForeignKey(related_name='django_velcro_datapublicationsrelationship_related_data', to='contenttypes.ContentType')),
                ('publications_content_type', models.ForeignKey(related_name='django_velcro_datapublicationsrelationship_related_publications', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataScientistsRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data_object_id', models.PositiveIntegerField()),
                ('scientists_object_id', models.PositiveIntegerField()),
                ('data_content_type', models.ForeignKey(related_name='django_velcro_datascientistsrelationship_related_data', to='contenttypes.ContentType')),
                ('scientists_content_type', models.ForeignKey(related_name='django_velcro_datascientistsrelationship_related_scientists', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicationsScientistsRelationship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('publications_object_id', models.PositiveIntegerField()),
                ('scientists_object_id', models.PositiveIntegerField()),
                ('publications_content_type', models.ForeignKey(related_name='django_velcro_publicationsscientistsrelationship_related_publications', to='contenttypes.ContentType')),
                ('scientists_content_type', models.ForeignKey(related_name='django_velcro_publicationsscientistsrelationship_related_scientists', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
