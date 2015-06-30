from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import DataScientistRelationship


class Scientist(models.Model):
    name = models.CharField(max_length=50)
    related_data = GenericRelation(DataScientistRelationship,
        content_type_field='data_content_type',
        object_id_field='data_object_id',
        related_query_name='scientists',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
