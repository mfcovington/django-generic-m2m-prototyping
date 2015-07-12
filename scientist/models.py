from django.conf import settings
from django.db import models

def relations_base(object_type):
    if 'django_velcro' in settings.INSTALLED_APPS:
        from django_velcro.utils import relations_abstract_base
        RelationsBase = relations_abstract_base(object_type,
            relationships=settings.RELATIONSHIPS)
    else:
        RelationsBase = models.Model
    return RelationsBase


class Scientist(relations_base('scientists')):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
