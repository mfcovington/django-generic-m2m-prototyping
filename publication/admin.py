from django.contrib import admin

from glue.admin import (PublicationsToDataRelationshipInline,
    PublicationsToScientistsRelationshipInline)
from genericadmin.admin import GenericAdminModelAdmin

from .models import Publication, PublicationSet

@admin.register(Publication, PublicationSet)
class PublicationAdmin(GenericAdminModelAdmin):
    inlines = [
        PublicationsToDataRelationshipInline,
        PublicationsToScientistsRelationshipInline,
    ]
