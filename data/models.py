from django.conf import settings
from django.db import models

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import relations_abstract_base
    DataRelationsBase = relations_abstract_base('data',
        relationships=settings.RELATIONSHIPS)
else:
    DataRelationsBase = models.Model


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
