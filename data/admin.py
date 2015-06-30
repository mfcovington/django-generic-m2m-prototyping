from django.contrib import admin

from glue.admin import (DataToPublicationRelationshipInline,
    DataToScientistRelationshipInline)
from genericadmin.admin import GenericAdminModelAdmin

from .models import Data, DataSet

@admin.register(Data, DataSet)
class DataAdmin(GenericAdminModelAdmin):
    inlines = [
        DataToPublicationRelationshipInline,
        DataToScientistRelationshipInline
    ]
