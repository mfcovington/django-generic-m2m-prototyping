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
