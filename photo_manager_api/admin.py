from django.contrib import admin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_created', 'description')
    list_filter = ('id', 'user_created', 'location', 'description', 'people_on_photo')
    search_fields = ('id', 'user_created')
