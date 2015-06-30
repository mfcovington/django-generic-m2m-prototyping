from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Scientist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
