from django.conf import settings
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin

from .models import Publication, PublicationSet


@admin.register(Publication, PublicationSet)
class PublicationAdmin(GenericAdminModelAdmin):
    if 'glue' in settings.INSTALLED_APPS:
        from glue.relationships import RELATIONSHIPS
        from glue.utils import get_relationship_inlines
        inlines = get_relationship_inlines('publications', relationships=RELATIONSHIPS)
