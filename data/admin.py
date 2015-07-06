from django.conf import settings
from django.contrib import admin

from .models import Data, DataSet

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import generic_admin_base
    DataGenericAdminBase = generic_admin_base('data',
        relationships=settings.RELATIONSHIPS)
else:
    DataGenericAdminBase = admin.ModelAdmin


@admin.register(Data, DataSet)
class DataAdmin(DataGenericAdminBase):
    pass
