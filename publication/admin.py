from django.conf import settings
from django.contrib import admin

from .models import Publication, PublicationSet

def admin_base(object_type):
    if 'django_velcro' in settings.INSTALLED_APPS:
        from django_velcro.utils import generic_admin_base
        GenericAdminBase = generic_admin_base(object_type)
    else:
        GenericAdminBase = admin.ModelAdmin
    return GenericAdminBase


@admin.register(Publication, PublicationSet)
class PublicationAdmin(admin_base('publications')):
    pass
