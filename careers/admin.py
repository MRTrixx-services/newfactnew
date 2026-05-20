from django.contrib import admin
from django.utils.html import format_html

from .models import (
    CareerHero,
    WhyJoinUs,
    JobOpening,
    Internship,
    CompanyCulture,
    HRContact,
    CareerApplication,
)


@admin.register(CareerHero)
class CareerHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'hero_image_preview']

    def hero_image_preview(self, obj):
        if obj.background_image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;" />',
                obj.background_image.url
            )
        return "No Image"

    hero_image_preview.short_description = "Preview"


@admin.register(WhyJoinUs)
class WhyJoinUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon']


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'department',
        'location',
        'salary',
        'is_active',
        'created_at'
    ]

    list_filter = ['is_active', 'department']
    search_fields = ['title', 'department', 'location']


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'duration',
        'stipend',
        'is_active'
    ]


@admin.register(CompanyCulture)
class CompanyCultureAdmin(admin.ModelAdmin):
    list_display = ['title', 'culture_image_preview']

    def culture_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;" />',
                obj.image.url
            )
        return "No Image"

    culture_image_preview.short_description = "Preview"


@admin.register(HRContact)
class HRContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone',
        'job',
        'applied_at'
    ]

    readonly_fields = ['applied_at']

    search_fields = [
        'full_name',
        'email',
        'phone'
    ]

    list_filter = ['applied_at']

    def resume_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank">Download Resume</a>',
                obj.resume.url
            )
        return "No Resume"

    resume_link.short_description = "Resume"