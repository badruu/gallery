from django.contrib import admin
from .models import Photo, Location, Category


class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)


admin.site.register(Photo,PhotoAdmin)
admin.site.register(Location)
admin.site.register(Category)