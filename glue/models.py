import operator
from functools import reduce

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .relationships import LIMITS, RELATIONSHIPS


############################################################
# RELATIONSHIP CLASS GENERATOR                             #
############################################################
# Define relationships & choice limits in relationships.py #
############################################################


def generate_relationship_model(relationship):
    content_1, content_2 = sorted(relationship)
    klass_name = '{}{}Relationship'.format(content_1.capitalize(),
        content_2.capitalize())
    typedict = {'__module__': __name__,}

    for content in map(lambda x: x.lower(), relationship):
        queries = []
        for lim in LIMITS[content]:
            queries.append(models.Q(**lim))
        limit = reduce(operator.or_, queries, models.Q())

        typedict.update({
            '{}_content_type'.format(content): models.ForeignKey(ContentType,
                limit_choices_to=limit,
                related_name='%(app_label)s_%(class)s_related_{}'.format(content)),
            '{}_object_id'.format(content): models.PositiveIntegerField(),
            '{}_content_object'.format(content): GenericForeignKey(
                '{}_content_type'.format(content), '{}_object_id'.format(content)),
        })

    def __str__(self):
        return '{}: {} ⟷  {}: {}'.format(
            getattr(self, '{}_content_type'.format(content_1)).name.upper(),
            getattr(self, '{}_content_object'.format(content_1)),
            getattr(self, '{}_content_type'.format(content_2)).name.upper(),
            getattr(self, '{}_content_object'.format(content_2)),
        )

    typedict['__str__'] = __str__
    klass = type(klass_name, (models.Model,), typedict)
    globals()[klass_name] = klass


####################
# GENERATE CLASSES #
####################


for r in RELATIONSHIPS:
    generate_relationship_model(r)
