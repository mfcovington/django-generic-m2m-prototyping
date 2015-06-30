from django.contrib import admin

from glue.admin import (PublicationToDataRelationshipInline,
    PublicationToScientistRelationshipInline)
from genericadmin.admin import GenericAdminModelAdmin

from .models import Publication, PublicationSet

@admin.register(Publication, PublicationSet)
class PublicationAdmin(GenericAdminModelAdmin):
    inlines = [
        PublicationToDataRelationshipInline,
        PublicationToScientistRelationshipInline,
    ]
