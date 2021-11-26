from django.contrib import admin
from .models import *
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportMixin
from accounts.models import CustomUser
from .models import T10_area

class t10Admin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['t10_area_prefecture', 't10_area_name', 't10_create_at', 't10_update_at']

class t9Admin(ImportExportMixin,admin.ModelAdmin):
    list_display=["t9_food_category_name","t9_create_at","t9_update_at" ]

class t8Admin(ImportExportMixin,admin.ModelAdmin):
    list_display=["t8_shop_category_name","t8_create_at","t8_update_at" ]

admin.site.register(T10_area, t10Admin)
admin.site.register(T9_food_category,t9Admin)



admin.site.register(T8_shop_category,t8Admin)
admin.site.register(T1_shop)

admin.site.register(T4_food)
admin.site.register(T5_user)
admin.site.register(T2_order)
admin.site.register(T3_order_detail)
admin.site.register(T6_review)
admin.site.register(T11_love)
admin.site.register(T12_charge)
admin.site.register(T13_inquiry)
admin.site.register(T7_delivery_man)
