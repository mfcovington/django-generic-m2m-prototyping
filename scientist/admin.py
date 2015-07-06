from django.conf import settings
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin

from .models import Scientist


@admin.register(Scientist)
class ScientistAdmin(GenericAdminModelAdmin):
    if 'django_velcro' in settings.INSTALLED_APPS:
        from django_velcro.utils import get_relationship_inlines
        inlines = get_relationship_inlines('scientists',
            relationships=settings.RELATIONSHIPS)
