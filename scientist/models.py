from django.conf import settings
from django.db import models

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import relations_abstract_base
    ScientistRelationsBase = relations_abstract_base('scientists',
        relationships=settings.RELATIONSHIPS)
else:
    ScientistRelationsBase = models.Model


class Scientist(ScientistRelationsBase):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
