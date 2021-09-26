from django.contrib import admin
from .models import Sneaker, SneakerImage, SneakerSize


class SizeInline(admin.StackedInline):
    model = SneakerSize
    extra = 1


class ImageInline(admin.StackedInline):
    model = SneakerImage
    extra = 1


class SneakerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Se il titolo occupa solo una riga, selezionare Fill line', {'fields': ['name', 'fill_line', 'stockx', 'g_im']}),
        ]
    inlines = [SizeInline, ImageInline]

    list_display = ['name', 'available_pieces', 'sold_out']



admin.site.register(Sneaker, SneakerAdmin)


