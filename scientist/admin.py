from django.contrib import admin

from glue.admin import (ScientistsToDataRelationshipInline,
    ScientistsToPublicationsRelationshipInline)
from genericadmin.admin import GenericAdminModelAdmin

from .models import Scientist

@admin.register(Scientist)
class ScientistAdmin(GenericAdminModelAdmin):
    inlines = [
        ScientistsToDataRelationshipInline,
        ScientistsToPublicationsRelationshipInline,
    ]
