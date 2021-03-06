from django.contrib import admin
from . import models


@admin.register(models.YoutubeVideo)
class YoutubeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status', 'tags']
    list_display = ['slug', 'status', 'date', 'date_published', 'is_active']
    readonly_fields = ['date_created']
    fieldsets = (
        ('Visibility', {
            'classes': ('wide',),
            'fields': ('date_created', 'status', 'date_published')
            }
         ),
        ('Meta', {'fields': ('date', 'meta_description', 'icon', 'tags')},),
        ('Content', {'fields': ('youtube_id', 'title', 'slug',
                                'subtitle', 'content')},)
    )


@admin.register(models.FlickrAlbum)
class FlickrAlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status', 'tags']
    list_display = ['slug', 'status', 'date', 'date_published', 'is_active']
    readonly_fields = ['date_created']
    fieldsets = (
        ('Visibility', {
            'classes': ('wide',),
            'fields': ('date_created', 'status', 'date_published')
            }
         ),
        ('Meta', {'fields': ('date', 'meta_description', 'icon', 'tags')},),
        ('Content', {'fields': ('title', 'flickr_album_url', 'slug',
                                'flickr_thumbnail_url',
                                'subtitle', 'content')},),
    )


@admin.register(models.PressEntry)
class PressAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'date_published']
    list_filter = ['status', 'tags']
    list_display = ['slug', 'status', 'date', 'date_published', 'is_active']
    readonly_fields = ['date_created']
    fieldsets = (
        ('Visibility', {
            'classes': ('wide',),
            'fields': ('date_created', 'status', 'date_published')
            }
         ),
        ('Meta', {'fields': ('date', 'meta_description', 'icon', 'tags')},),
        ('Content', {'fields': ('external_url', 'title', 'slug',
                                'subtitle', 'content')},)
    )


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['slug', 'title', 'date_created', 'blurb']
    list_display = ['slug', 'title', 'date_created']
