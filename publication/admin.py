from django.conf import settings
from django.contrib import admin

from .models import Publication, PublicationSet

if 'django_velcro' in settings.INSTALLED_APPS:
    from django_velcro.utils import generic_admin_base
    PublicationGenericAdminBase = generic_admin_base('publications',
        relationships=settings.RELATIONSHIPS)
else:
    PublicationGenericAdminBase = admin.ModelAdmin


@admin.register(Publication, PublicationSet)
class PublicationAdmin(PublicationGenericAdminBase):
    pass
