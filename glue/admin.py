from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from .models import (DataPublicationRelationship, DataScientistRelationship,
    RelatedContent)


#######################
# INLINE BASE CLASSES #
#######################


class FromData():
    ct_field = 'data_content_type'
    ct_fk_field = 'data_object_id'


class FromPublication():
    ct_field = 'publications_content_type'
    ct_fk_field = 'publications_object_id'


class FromScientist():
    ct_field = 'scientists_content_type'
    ct_fk_field = 'scientists_object_id'


class ToData():
    ordering = ['data_content_type']


class ToPublication():
    ordering = ['publications_content_type']


class ToScientist():
    ordering = ['scientists_content_type']


############################
# COMPOSITE INLINE CLASSES #
############################


class DataToPublicationRelationshipInline(FromData, ToPublication,
    GenericTabularInline):

    model = DataPublicationRelationship


class DataToScientistRelationshipInline(FromData, ToScientist,
    GenericTabularInline):

    model = DataScientistRelationship


class PublicationToDataRelationshipInline(FromPublication, ToData,
    GenericTabularInline):

    model = DataPublicationRelationship


class ScientistToDataRelationshipInline(FromScientist, ToData,
    GenericTabularInline):

    model = DataScientistRelationship


#################
# ADMIN CLASSES #
#################


@admin.register(DataPublicationRelationship)
class DataPublicationsAdmin(GenericAdminModelAdmin):
    pass


@admin.register(DataScientistRelationship)
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
