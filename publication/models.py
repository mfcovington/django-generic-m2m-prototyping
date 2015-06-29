from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import DataPublicationRelationship

class Publication(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField()
    data = GenericRelation(DataPublicationRelationship, related_query_name='publications')

    def __str__(self):
        return self.name
