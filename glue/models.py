from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class RelatedContent(models.Model):
    """
    Relates any one entry to another entry irrespective of their individual models.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent_content_type = models.ForeignKey(ContentType, related_name="parent_test_link")
    parent_object_id = models.PositiveIntegerField()
    parent_content_object = GenericForeignKey('parent_content_type', 'parent_object_id')

    def __str__(self):
        return "{}: {}".format(self.content_type.name, self.content_object)


################
# BASE CLASSES #
################


class DataRelationshipBase(models.Model):
    data_limit = models.Q(app_label='data', model='data') | \
        models.Q(app_label='data', model='dataset')
    data_content_type = models.ForeignKey(ContentType, limit_choices_to=data_limit, related_name='%(app_label)s_%(class)s_related_data')
    data_object_id = models.PositiveIntegerField()
    data_content_object = GenericForeignKey('data_content_type', 'data_object_id')

    def data_identifier(self):
        return "{}: {}".format(self.data_content_type.name.upper(), self.data_content_object)

    class Meta:
        abstract = True


class PublicationRelationshipBase(models.Model):
    publications_limit = models.Q(app_label='publication', model='publication') | \
        models.Q(app_label='publication', model='publicationset')
    publications_content_type = models.ForeignKey(ContentType, limit_choices_to=publications_limit, related_name='%(app_label)s_%(class)s_related_publications')
    publications_object_id = models.PositiveIntegerField()
    publications_content_object = GenericForeignKey('publications_content_type', 'publications_object_id')

    def publications_identifier(self):
        return "{}: {}".format(self.publications_content_type.name.upper(), self.publications_content_object)

    class Meta:
        abstract = True


class ScientistRelationshipBase(models.Model):
    scientists_limit = models.Q(app_label='scientist', model='scientist')
    scientists_content_type = models.ForeignKey(ContentType, limit_choices_to=scientists_limit, related_name='%(app_label)s_%(class)s_related_scientists')
    scientists_object_id = models.PositiveIntegerField()
    scientists_content_object = GenericForeignKey('scientists_content_type', 'scientists_object_id')

    def scientists_identifier(self):
        return "{}: {}".format(self.scientists_content_type.name.upper(), self.scientists_content_object)

    class Meta:
        abstract = True


#####################
# COMPOSITE CLASSES #
#####################


class DataPublicationRelationship(DataRelationshipBase, PublicationRelationshipBase):

    def __str__(self):
        return "{} ⟷ {}".format(self.data_identifier(), self.publications_identifier())


class DataScientistRelationship(DataRelationshipBase, ScientistRelationshipBase):

    def __str__(self):
        return "{} ⟷ {}".format(self.data_identifier(), self.scientists_identifier())


class PublicationScientistRelationship(PublicationRelationshipBase, ScientistRelationshipBase):

    def __str__(self):
        return "{} ⟷ {}".format(self.publications_identifier(), self.scientists_identifier())
