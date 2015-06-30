from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from .models import (DataPublicationsRelationship, DataScientistsRelationship,
    PublicationsScientistsRelationship, RelatedContent)


#######################
# INLINE BASE CLASSES #
#######################


class FromData():
    ct_field = 'data_content_type'
    ct_fk_field = 'data_object_id'


class FromPublications():
    ct_field = 'publications_content_type'
    ct_fk_field = 'publications_object_id'


class FromScientists():
    ct_field = 'scientists_content_type'
    ct_fk_field = 'scientists_object_id'


class ToData():
    ordering = ['data_content_type']


class ToPublications():
    ordering = ['publications_content_type']


class ToScientists():
    ordering = ['scientists_content_type']


############################
# COMPOSITE INLINE CLASSES #
############################


class DataToPublicationsRelationshipInline(FromData, ToPublications,
    GenericTabularInline):

    model = DataPublicationsRelationship


class DataToScientistsRelationshipInline(FromData, ToScientists,
    GenericTabularInline):

    model = DataScientistsRelationship


class PublicationsToDataRelationshipInline(FromPublications, ToData,
    GenericTabularInline):

    model = DataPublicationsRelationship


class PublicationsToScientistsRelationshipInline(FromPublications, ToScientists,
    GenericTabularInline):

    model = PublicationsScientistsRelationship


class ScientistsToDataRelationshipInline(FromScientists, ToData,
    GenericTabularInline):

    model = DataScientistsRelationship


class ScientistsToPublicationsRelationshipInline(FromScientists, ToPublications,
    GenericTabularInline):

    model = PublicationsScientistsRelationship


#################
# ADMIN CLASSES #
#################


@admin.register(DataPublicationsRelationship)
class DataPublicationsAdmin(GenericAdminModelAdmin):
    pass


@admin.register(PublicationsScientistsRelationship)
class PublicationsScientistsAdmin(GenericAdminModelAdmin):
    pass


@admin.register(DataScientistsRelationship)
class DataScientistsAdmin(GenericAdminModelAdmin):
    pass
class RelatedContentInline(GenericTabularInline):
    model = RelatedContent
    ct_field = 'parent_content_type' # See below (1).
    ct_fk_field = 'parent_object_id' # See below (1).


@admin.register(RelatedContent)
class RelatedContentAdmin(GenericAdminModelAdmin): # Super important! See below (2).
    content_type_whitelist = ('data/Data', 'publication/Publication' ) # Add white/black lists on this class
    inlines = [RelatedContentInline,]
