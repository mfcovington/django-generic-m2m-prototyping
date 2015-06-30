from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import (DataPublicationsRelationship,
    PublicationsScientistsRelationship)


class PublicationRelationsBase(models.Model):
    related_data = GenericRelation(DataPublicationsRelationship,
        content_type_field='data_content_type',
        object_id_field='data_object_id',
        related_query_name='publications',
    )
    related_scientists = GenericRelation(PublicationsScientistsRelationship,
        content_type_field='scientists_content_type',
        object_id_field='scientists_object_id',
        related_query_name='publications',
    )

    class Meta:
        abstract = True


class Publication(PublicationRelationsBase):
    name = models.CharField(max_length=50,)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PublicationSet(PublicationRelationsBase):
    name = models.CharField(max_length=50,)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
