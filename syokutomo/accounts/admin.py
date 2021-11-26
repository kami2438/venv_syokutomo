from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import *
class t10Admin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['t10_area_prefecture', 't10_area_name', 't10_create_at', 't10_update_at']
admin.site.register(T10_area, t10Admin)
admin.site.register(CustomUser)