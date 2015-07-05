from django.conf import settings
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin

from .models import Scientist


@admin.register(Scientist)
class ScientistAdmin(GenericAdminModelAdmin):
    if 'glue' in settings.INSTALLED_APPS:
        from glue.relationships import RELATIONSHIPS
        from glue.utils import get_relationship_inlines
        inlines = get_relationship_inlines('scientists', relationships=RELATIONSHIPS)
