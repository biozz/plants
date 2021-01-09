from django.contrib import admin

from .forms import PlantAdminForm
from .models import Image, Plant


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class PlantAdmin(admin.ModelAdmin):
    form = PlantAdminForm
    # inlines = [ImageInline]

    list_display = ("name", "name_lat", "name_en", "name_alt")


admin.site.register(Plant, PlantAdmin)
