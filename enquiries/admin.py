from django.contrib import admin
from .models import Enquiry, Project

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at", "is_reviewed")
    list_filter = ("service", "is_reviewed", "created_at")
    search_fields = ("name", "email", "organization", "message")
    readonly_fields = ("created_at",)
    list_editable = ("is_reviewed",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "status")
    prepopulated_fields = {"slug": ("title",)}