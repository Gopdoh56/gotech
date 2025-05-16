# landing_page/models.py
from django.db import models
from django.utils import timezone

class FreeWebsiteSubmission(models.Model):
    # Basic Info
    full_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=150,blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    # Business Description
    business_description = models.TextField(blank=True, null=True,help_text="Describe your business or organization.")
    services_offered = models.TextField(blank=True, null=True,help_text="What are your main services or products?")

    # Reasons for Website (Checkboxes - stored as comma-separated string or multiple booleans)
    # For simplicity with ModelForms, let's use multiple BooleanFields.
    # A ManyToManyField to a "Reason" model would be more robust but more complex for a simple form.
    reason_online_presence = models.BooleanField(default=False, verbose_name="Establish an online presence")
    reason_wider_audience = models.BooleanField(default=False, verbose_name="Reach a wider audience")
    reason_leads_sales = models.BooleanField(default=False, verbose_name="Generate leads and sales")
    reason_provide_info = models.BooleanField(default=False, verbose_name="Provide information to customers")
    reason_brand_awareness = models.BooleanField(default=False, verbose_name="Build brand awareness")
    reason_showcase_products = models.BooleanField(default=False, verbose_name="Showcase products/services")
    reason_other = models.CharField(max_length=255, blank=True, null=True, verbose_name="Other reason (Specify)")

    # Main Goals (This is tricky for "rank in order". We'll simplify for now)
    # Storing ranked goals directly in a simple model is complex.
    # For now, let's ask for their TOP goal as a start, or a text area for them to list.
    # A more complex solution would involve JavaScript and potentially a JSONField or related models.
    main_goal_for_website = models.TextField(
        blank=True, null=True,
        help_text="What are your main goals for your website? Please list them, or describe your top priority."
    )
    # We can add specific goal fields later if needed for filtering, e.g.:
    # goal_generate_leads = models.BooleanField(default=False, verbose_name="Generate leads/inquiries")
    # goal_increase_sales = models.BooleanField(default=False, verbose_name="Increase sales/bookings")
    # ... and then a field for 'other_goal_specify'

    # Branding & Content
    has_logo = models.BooleanField(default=False, verbose_name="Do you have a logo?")
    has_brand_colors_fonts = models.BooleanField(default=False, verbose_name="Do you have brand colors and fonts?")
    will_provide_content = models.BooleanField(default=False, verbose_name="Are you willing to provide all the content (text and images) for your website?")

    # Testimonial
    willing_to_provide_testimonial = models.BooleanField(default=False, verbose_name="Are you willing to provide a written or video testimonial if satisfied?")

    # Existing Presence
    existing_website_url = models.URLField(blank=True, null=True, verbose_name="Existing Website (if any)")
    social_media_links = models.TextField(blank=True, null=True, help_text="Links to your social media profiles (e.g., Facebook, Instagram, LinkedIn), one per line.")

    # Target Audience
    target_audience_description = models.TextField(blank=True, null=True, help_text="Briefly describe your target audience or ideal customer.")

    # Competitors
    key_competitors = models.TextField(blank=True, null=True, help_text="List 1-3 key competitors or websites you admire (and why, if possible).")

    # Additional Comments
    additional_comments = models.TextField(blank=True, null=True)

    # Admin fields (unchanged from before)
    submission_date = models.DateTimeField(default=timezone.now)
    contacted_for_website = models.BooleanField(default=False, help_text="Check this if you've contacted them about the free website.")
    website_built = models.BooleanField(default=False, help_text="Check this if the free website has been built.")

    def __str__(self):
        return f"{self.business_name} ({self.full_name}) - Submitted: {self.submission_date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Free Website Submission"
        verbose_name_plural = "Free Website Submissions"
        ordering = ['-submission_date']