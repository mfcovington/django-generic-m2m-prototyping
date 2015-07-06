from django.conf import settings
from django.contrib import admin

from .models import Scientist

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import generic_admin_base
    ScientistGenericAdminBase = generic_admin_base('scientists',
        relationships=settings.RELATIONSHIPS)
else:
    ScientistGenericAdminBase = admin.ModelAdmin


@admin.register(Scientist)
class ScientistAdmin(ScientistGenericAdminBase):
    pass
