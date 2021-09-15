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
<<<<<<< Updated upstream
        ('Se il nome non occupa più di una riga, selezionare Fill lines', {'fields': ['name', 'fill_lines']}),
=======
        (None, {'fields': ['name', 'fill_line']}),
>>>>>>> Stashed changes
        ]
    inlines = [SizeInline, ImageInline]

    list_display = ['name', 'available_pieces', 'sold_out']



admin.site.register(Sneaker, SneakerAdmin)


