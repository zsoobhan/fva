from django.contrib import admin
from . import models


@admin.register(models.YoutubeVideo)
class YoutubeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status']
    list_display = ['slug', 'status', 'date', 'date_published', 'is_active']
    readonly_fields = ['date_created']
    fieldsets = (
        ('Internal', {
            'classes': ('wide',),
            'fields': ('date_created', 'slug', 'status', 'date_published')
            }
         ),
        ('Meta', {'fields': ('date', 'meta_description', 'icon', 'tags')},),
        ('Content', {'fields': ('youtube_id', 'title',
                                'subtitle', 'content')},)
    )


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'blurb']
    list_display = ['slug', 'title', 'date_created']
