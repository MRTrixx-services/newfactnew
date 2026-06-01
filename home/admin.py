
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Slider,
    HomeContent,
    ServicePageIntro,
    Service,
    ProjectsPage,
    Project,
    SocialServicesPage,
    SocialService
)


# =========================================
# COMMON MEDIA PREVIEW
# =========================================
def media_preview(obj, image_field='image', video_field='video'):

    image = getattr(obj, image_field, None)
    video = getattr(obj, video_field, None)

    # VIDEO PREVIEW
    if video:
        return format_html(
            '''
            <video width="120" height="70" controls>
                <source src="{}" type="video/mp4">
            </video>
            ''',
            video.url
        )

    # IMAGE PREVIEW
    if image:
        return format_html(
            '<img src="{}" style="height:70px; border-radius:8px;" />',
            image.url
        )

    return "-"

media_preview.short_description = "Preview"


# =========================================
# SLIDER
# =========================================
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(obj)

    list_display = [
        'title',
        'preview',
        'is_active',
        'order'
    ]

    list_editable = [
        'is_active',
        'order'
    ]


# =========================================
# HOME CONTENT
# =========================================
@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):

    list_display = ['__str__']


# =========================================
# SERVICE PAGE INTRO
# =========================================
@admin.register(ServicePageIntro)
class ServicePageIntroAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(
            obj,
            image_field='center_image',
            video_field='center_video'
        )

    list_display = [
        '__str__',
        'preview'
    ]


# =========================================
# SERVICE
# =========================================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(obj)

    list_display = [
        'title',
        'preview',
        'is_featured',
        'order'
    ]

    list_editable = [
        'is_featured',
        'order'
    ]

    search_fields = ['title']


# =========================================
# PROJECTS PAGE
# =========================================
@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(
            obj,
            image_field='hero_image',
            video_field='hero_video'
        )

    list_display = [
        '__str__',
        'preview'
    ]


# =========================================
# PROJECT
# =========================================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(obj)

    list_display = [
        'title',
        'preview',
        'status',
        'project_date',
        'order'
    ]

    list_filter = ['status']

    list_editable = ['order']

    search_fields = ['title']

    prepopulated_fields = {
        'slug': ('title',)
    }


# =========================================
# SOCIAL SERVICES PAGE
# =========================================
@admin.register(SocialServicesPage)
class SocialServicesPageAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(
            obj,
            image_field='hero_image',
            video_field='hero_video'
        )

    list_display = [
        '__str__',
        'preview'
    ]


# =========================================
# SOCIAL SERVICE
# =========================================
@admin.register(SocialService)
class SocialServiceAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return media_preview(obj)

    list_display = [
        'title',
        'preview',
        'status',
        'project_date',
        'order'
    ]

    list_filter = ['status']

    list_editable = ['order']

    search_fields = ['title']

    prepopulated_fields = {
        'slug': ('title',)
    }

