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
