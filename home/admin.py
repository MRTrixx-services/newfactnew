from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Slider, HomeContent,
    ServicePageIntro, Service,
    ProjectsPage, Project,
    SocialServicesPage, SocialService
)


# =========================================
# HELPER
# =========================================
def image_preview(obj):
    if obj.image:
        return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.image.url)
    return '-'
image_preview.short_description = 'Preview'


# =========================================
# SLIDER
# =========================================
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    list_display = ['title', image_preview, 'is_active']
    list_editable = ['is_active']


# =========================================
# HOME CONTENT
# =========================================
admin.site.register(HomeContent)


# =========================================
# SERVICE PAGE INTRO
# =========================================
@admin.register(ServicePageIntro)
class ServicePageIntroAdmin(admin.ModelAdmin):

    def center_image_preview(self, obj):
        if obj.center_image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.center_image.url)
        return '-'
    center_image_preview.short_description = 'Center Image'

    list_display = ['__str__', 'center_image_preview']


# =========================================
# SERVICE
# =========================================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'

    list_display = ['title', 'image_preview', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']


# =========================================
# PROJECTS PAGE
# =========================================
@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):

    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.hero_image.url)
        return '-'
    hero_preview.short_description = 'Hero Image'

    list_display = ['__str__', 'hero_preview']


# =========================================
# PROJECT
# =========================================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'

    list_display = ['title', 'image_preview', 'status', 'project_date', 'order']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order']


# =========================================
# SOCIAL SERVICES PAGE
# =========================================
@admin.register(SocialServicesPage)
class SocialServicesPageAdmin(admin.ModelAdmin):

    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.hero_image.url)
        return '-'
    hero_preview.short_description = 'Hero Image'

    list_display = ['__str__', 'hero_preview']


# =========================================
# SOCIAL SERVICE
# =========================================
@admin.register(SocialService)
class SocialServiceAdmin(admin.ModelAdmin):

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;"/>', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'

    list_display = ['title', 'image_preview', 'status', 'project_date', 'order']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order']
