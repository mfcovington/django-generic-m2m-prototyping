from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from .models import DataPublicationRelationship, RelatedContent


class PublicationToDataRelationshipInline(GenericTabularInline):
    model = DataPublicationRelationship
    ct_field = 'publication_content_type'
    ct_fk_field = 'publication_object_id'


class DataToPublicationRelationshipInline(GenericTabularInline):
    model = DataPublicationRelationship
    ct_field = 'data_content_type'
    ct_fk_field = 'data_object_id'


@admin.register(DataPublicationRelationship)
class DataPublicationsAdmin(GenericAdminModelAdmin):
    pass


class RelatedContentInline(GenericTabularInline):
    model = RelatedContent
    ct_field = 'parent_content_type' # See below (1).
    ct_fk_field = 'parent_object_id' # See below (1).


@admin.register(RelatedContent)
class RelatedContentAdmin(GenericAdminModelAdmin): # Super important! See below (2).
    content_type_whitelist = ('data/Data', 'publication/Publication' ) # Add white/black lists on this class
    inlines = [RelatedContentInline,]
