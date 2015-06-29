from django.contrib.contenttypes.models import ContentType

from .models import DataPublicationRelationship

def get_related_publications(data_object):
    data_content_type = ContentType.objects.get_for_model(data_object)
    data_publication_relationships = DataPublicationRelationship.objects.filter(
        data_content_type__pk=data_content_type.id, data_object_id=data_object.id)

    return [related.publication_content_object
        for related in sorted(data_publication_relationships,
            key=lambda x: x.publication_content_object.name.lower())]

def get_related_data(publication_object):
    publication_content_type = ContentType.objects.get_for_model(publication_object)
    data_publication_relationships = DataPublicationRelationship.objects.filter(
        publication_content_type__pk=publication_content_type.id, publication_object_id=publication_object.id)

    return [related.data_content_object
        for related in sorted(data_publication_relationships,
            key=lambda x: x.data_content_object.name.lower())]

def get_related_data_publication(object):
    content_type = ContentType.objects.get_for_model(object)
    class_name = type(object).__name__.lower()
    kwargs = {
        '{}_content_type__pk'.format(class_name): content_type.id,
        '{}_object_id'.format(class_name): object.id,
    }
    data_publication_relationships = DataPublicationRelationship.objects.filter(**kwargs)

    if class_name == 'data':
        related_class_name = 'publication'
    elif class_name == 'publication':
        related_class_name = 'data'
    # else:
        # Error

    related_content_object = '{}_content_object'.format(related_class_name)

    return [getattr(related, related_content_object)
        for related in sorted(data_publication_relationships,
            key=lambda x: getattr(x, related_content_object).name.lower())]

def get_related_content(related_type, object):
    """
    Usage:
        from data.models import Data
        data_object = Data.objects.first()
        get_related_content('publication', data_object)
    """
    content_type = ContentType.objects.get_for_model(object)
    class_name = type(object).__name__.lower()
    kwargs = {
        '{}_content_type__pk'.format(class_name): content_type.id,
        '{}_object_id'.format(class_name): object.id,
    }
    relationships = getattr(object, related_type).model.objects.filter(**kwargs)

    related_content_object = '{}_content_object'.format(related_type)

    return [getattr(related, related_content_object)
        for related in sorted(relationships,
            key=lambda x: (
                type(getattr(x, related_content_object)).__name__.lower(),
                getattr(x, related_content_object).name.lower()))]
