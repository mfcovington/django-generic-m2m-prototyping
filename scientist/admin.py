from django.conf import settings
from django.contrib import admin

from .models import Scientist

def admin_base(object_type):
    if 'django_velcro' in settings.INSTALLED_APPS:
        from django_velcro.utils import generic_admin_base
        GenericAdminBase = generic_admin_base(object_type)
    else:
        GenericAdminBase = admin.ModelAdmin
    return GenericAdminBase


@admin.register(Scientist)
class ScientistAdmin(admin_base('scientists')):
    pass
