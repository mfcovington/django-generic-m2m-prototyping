from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import DataPublicationRelationship, DataScientistRelationship


class DataRelationsBase(models.Model):
    related_publications = GenericRelation(DataPublicationRelationship,
        content_type_field='publications_content_type',
        object_id_field='publications_object_id',
        related_query_name='data',
    )
    related_scientists = GenericRelation(DataScientistRelationship,
        content_type_field='scientists_content_type',
        object_id_field='scientists_object_id',
        related_query_name='data',
    )

    class Meta:
        abstract = True


class Data(DataRelationsBase):
    name = models.CharField(max_length=50,)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class DataSet(DataRelationsBase):
    name = models.CharField(max_length=50,)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
