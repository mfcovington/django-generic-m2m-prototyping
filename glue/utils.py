from django.contrib.contenttypes.models import ContentType


def get_related_content(object, object_type, related_type):
    """
    Usage:
        from data.models import Data
        data_set = DataSet.objects.first()
        get_related_content(data_set, 'data', publication')
    """
    content_type = ContentType.objects.get_for_model(object)
    kwargs = {
        '{}_content_type__pk'.format(object_type): content_type.id,
        '{}_object_id'.format(object_type): object.id,
    }
    relationships = getattr(object,
        'related_{}'.format(related_type)).model.objects.filter(**kwargs)

    related_content_object = '{}_content_object'.format(related_type)

    return [getattr(related, related_content_object)
        for related in sorted(relationships,
            key=lambda x: (
                type(getattr(x, related_content_object)).__name__.lower(),
                getattr(x, related_content_object).name.lower()))]

def get_relationship_inlines(object_type, relationships=None, related_types=None):
    """
    Import relevant relationship inline models for an admin model.

    Usage:

        # glue/relationships.py:

        RELATIONSHIPS = [
            ('data', 'publications'),
            ('data', 'scientists'),
            ('publications', 'scientists'),
        ]

        # data/admin.py:

        @admin.register(Data, DataSet)
        class DataAdmin(GenericAdminModelAdmin):
            if 'glue' in settings.INSTALLED_APPS:
                from glue.relationships import RELATIONSHIPS
                from glue.utils import get_relationship_inlines
                inlines = get_relationship_inlines('data', relationships=RELATIONSHIPS)


    Equivalent To:

        # data/admin.py:

        from glue.admin import (DataToPublicationsRelationshipInline,
            DataToScientistsRelationshipInline)

        @admin.register(Data, DataSet)
        class DataAdmin(GenericAdminModelAdmin):
            inlines = [
                DataToPublicationsRelationshipInline,
                DataToScientistsRelationshipInline
            ]
    """
    related_types = validate_and_process_related(object_type, relationships,
        related_types)

    from importlib import import_module

    inlines = []
    for related in related_types:
        inline_class_name = '{}To{}RelationshipInline'.format(object_type.capitalize(), related.capitalize())
        inline_class = getattr(import_module('.admin', package=__package__),
            inline_class_name)
        globals()[inline_class_name] = inline_class
        inlines.append(inline_class)

    return inlines

def validate_and_process_related(object_type, relationships=[], related_types=[]):
    if relationships is None:
        relationships = []

    if related_types is None:
        related_types = []

    if (relationships and related_types) or (not relationships and not related_types):
        raise ValueError("Either 'relationships' or 'related_types' must be defined.")

    if relationships:
        for r in relationships:
            if object_type in r:
                related_types.extend([related for related in r
                    if related != object_type])
        related_types = sorted(related_types)

    return related_types
