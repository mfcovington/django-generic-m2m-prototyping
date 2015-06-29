from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import DataPublicationRelationship

class Data(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField()
    publication = GenericRelation(DataPublicationRelationship,
        content_type_field='publication_content_type',
        object_id_field='publication_object_id',
        related_query_name='data',
    )

    def __str__(self):
        return self.name
