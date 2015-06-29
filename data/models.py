from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import DataPublicationRelationship


class Data(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField()
    related_publications = GenericRelation(DataPublicationRelationship,
        content_type_field='publications_content_type',
        object_id_field='publications_object_id',
        related_query_name='data',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class DataSet(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField()
    related_publications = GenericRelation(DataPublicationRelationship,
        content_type_field='publications_content_type',
        object_id_field='publications_object_id',
        related_query_name='data',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
