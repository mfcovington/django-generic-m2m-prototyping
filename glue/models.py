from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class RelatedContent(models.Model):
    """
    Relates any one entry to another entry irrespective of their individual models.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent_content_type = models.ForeignKey(ContentType, related_name="parent_test_link")
    parent_object_id = models.PositiveIntegerField()
    parent_content_object = GenericForeignKey('parent_content_type', 'parent_object_id')

    def __str__(self):
        return "{}: {}".format(self.content_type.name, self.content_object)
