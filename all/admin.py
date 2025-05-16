# landing_page/admin.py
from django.contrib import admin
from .models import FreeWebsiteSubmission

@admin.register(FreeWebsiteSubmission)
class FreeWebsiteSubmissionAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'full_name', 'email', 'submission_date', 'contacted_for_website', 'website_built')
    list_filter = ('submission_date', 'industry', 'contacted_for_website', 'website_built', 'has_logo', 'will_provide_content', 'willing_to_provide_testimonial')
    search_fields = ('full_name', 'business_name', 'email', 'industry', 'project_description')
    list_editable = ('contacted_for_website', 'website_built')
    readonly_fields = ('submission_date',)

    fieldsets = (
        ('Applicant Information', {
            'fields': ('full_name', 'business_name', 'email', 'phone_number', 'industry', 'submission_date')
        }),
        ('Project Description', {
            'fields': ('business_description', 'services_offered', 'target_audience_description')
        }),
        ('Reasons for Website', {
            'fields': (
                'reason_online_presence', 'reason_wider_audience', 'reason_leads_sales',
                'reason_provide_info', 'reason_brand_awareness', 'reason_showcase_products',
                'reason_other'
            ),
            'classes': ('collapse',), # Makes this section collapsible
        }),
        ('Website Goals', {
            'fields': ('main_goal_for_website',),
             'classes': ('collapse',),
        }),
        ('Assets & Content Readiness', {
            'fields': ('has_logo', 'has_brand_colors_fonts', 'will_provide_content', 'willing_to_provide_testimonial'),
             'classes': ('collapse',),
        }),
        ('Existing Online Presence', {
            'fields': ('existing_website_url', 'social_media_links', 'key_competitors'),
             'classes': ('collapse',),
        }),
        ('Additional Information', {
            'fields': ('additional_comments',),
             'classes': ('collapse',),
        }),
        ('Campaign Status (Admin)', {
            'fields': ('contacted_for_website', 'website_built')
        }),
    )