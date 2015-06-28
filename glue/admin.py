from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from .models import RelatedContent

class RelatedContentInline(GenericTabularInline):
    model = RelatedContent
    ct_field = 'parent_content_type' # See below (1).
    ct_fk_field = 'parent_object_id' # See below (1).

@admin.register(RelatedContent)
class RelatedContentAdmin(GenericAdminModelAdmin): # Super important! See below (2).
    content_type_whitelist = ('data/Data', 'publication/Publication' ) # Add white/black lists on this class
    inlines = [RelatedContentInline,]
