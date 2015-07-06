from django.conf import settings
from django.db import models

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import relations_abstract_base
    PublicationRelationsBase = relations_abstract_base('publications',
        relationships=settings.RELATIONSHIPS)
else:
    PublicationRelationsBase = models.Model


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
