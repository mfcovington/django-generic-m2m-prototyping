from django.contrib import admin

from glue.admin import RelatedContentInline
from genericadmin.admin import GenericAdminModelAdmin

from .models import Publication

@admin.register(Publication)
class PublicationAdmin(GenericAdminModelAdmin):
    inlines = [RelatedContentInline]
