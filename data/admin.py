from django.conf import settings
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin

from .models import Data, DataSet


@admin.register(Data, DataSet)
class DataAdmin(GenericAdminModelAdmin):
    if 'django_velcro' in settings.INSTALLED_APPS:
        from django_velcro.utils import get_relationship_inlines
        inlines = get_relationship_inlines('data',
            relationships=settings.RELATIONSHIPS)
