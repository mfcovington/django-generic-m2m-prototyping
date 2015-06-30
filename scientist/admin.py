from django.contrib import admin

from .models import Scientist

@admin.register(Scientist)
class ScientistAdmin(admin.ModelAdmin):
    pass
