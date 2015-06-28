from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from glue.models import RelatedContent

class Data(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField()
    publication = GenericRelation(RelatedContent, related_query_name='data')

    def __str__(self):
        return self.name
