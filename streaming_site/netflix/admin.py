from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'video_count', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active']
    
    def video_count(self, obj):
        return obj.videos.count()
    video_count.short_description = 'Videos'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'thumbnail_preview', 
        'title', 
        'video_type', 
        'year', 
        'rating_display',
        'duration_display',
        'view_count',
        'is_featured',
        'is_active'
    ]
    list_filter = ['video_type', 'is_featured', 'is_active', 'year', 'age_rating', 'categories']
    search_fields = ['title', 'description', 'director', 'cast', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories']
    list_editable = ['is_featured', 'is_active']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'video_type')
        }),
        ('Media Files', {
            'fields': ('thumbnail', 'hero_image', 'video_url', 'trailer_url')
        }),
        ('Metadata', {
            'fields': ('year', 'duration_minutes', 'rating_percentage', 'age_rating')
        }),
        ('Categorization', {
            'fields': ('categories', 'tags')
        }),
        ('AI Features', {
            'fields': ('ai_recommendation_score', 'ai_content_tags'),
            'classes': ('collapse',),
            'description': 'AI-powered features for enhanced content discovery'
        }),
        ('Credits', {
            'fields': ('director', 'cast', 'language'),
            'classes': ('collapse',)
        }),
        ('Status & Analytics', {
            'fields': ('is_featured', 'is_active', 'view_count')
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="width: 50px; height: 75px; object-fit: cover; border-radius: 4px;" />',
                obj.thumbnail
            )
        return '-'
    thumbnail_preview.short_description = 'Thumbnail'
    
    def rating_display(self, obj):
        color = 'green' if obj.rating_percentage >= 70 else 'orange' if obj.rating_percentage >= 50 else 'red'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}%</span>',
            color,
            obj.rating_percentage
        )
    rating_display.short_description = 'Rating'
    
    def duration_display(self, obj):
        return obj.get_duration_display()
    duration_display.short_description = 'Duration'
    
    # Customize admin site header
    admin.site.site_header = "StreamFlix Admin Panel"
    admin.site.site_title = "StreamFlix Admin"
    admin.site.index_title = "Content Management System"
