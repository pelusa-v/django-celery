from django.contrib import admin
from .models import ModelSitePort

# Register your models here.
class ModelSitePortAdmin(admin.ModelAdmin):
    list_display = ("modelSite", "equipmentModel", "equipmentModelSlot", "BoardModel", "port", "portType")

admin.site.register(ModelSitePort, ModelSitePortAdmin)