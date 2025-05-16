# landing_page/forms.py
from django import forms
from .models import FreeWebsiteSubmission

class FreeWebsiteForm(forms.ModelForm):
    # For the "Why do you want a website?" section (checkboxes)
    # We will render these manually in the template for better layout if needed,
    # but they are part of the model, so ModelForm will handle them.

    # For "Main Goals" - using the simplified TextField for now.

    class Meta:
        model = FreeWebsiteSubmission
        fields = [
            'full_name', 'business_name', 'email', 'phone_number', 'industry',
            'business_description', 'services_offered',
            'reason_online_presence', 'reason_wider_audience', 'reason_leads_sales',
            'reason_provide_info', 'reason_brand_awareness', 'reason_showcase_products',
            'reason_other',
            'main_goal_for_website',
            'has_logo', 'has_brand_colors_fonts', 'will_provide_content',
            'willing_to_provide_testimonial',
            'existing_website_url', 'social_media_links',
            'target_audience_description', 'key_competitors',
            'additional_comments',
        ]

        widgets = {
            # Basic Info
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'placeholder': 'Your Business or Organization Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your Phone Number (Optional)', 'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'placeholder': 'e.g., Retail, Non-profit, Personal Blog', 'class': 'form-control'}),

            # Business Description
            'business_description': forms.Textarea(attrs={'placeholder': 'Tell us about what you do...', 'rows': 4, 'class': 'form-control'}),
            'services_offered': forms.Textarea(attrs={'placeholder': 'List your key services or products...', 'rows': 3, 'class': 'form-control'}),

            # Reasons for Website (Checkboxes will use default rendering, can be customized in template)
            'reason_other': forms.TextInput(attrs={'placeholder': 'If other, please specify', 'class': 'form-control'}),

            # Main Goals
            'main_goal_for_website': forms.Textarea(attrs={'placeholder': 'e.g., Generate leads, Increase online sales, Provide information. Please list in order of importance or describe your top goal.', 'rows': 4, 'class': 'form-control'}),

            # Branding & Content (Checkboxes will use default rendering)

            # Testimonial (Checkbox)

            # Existing Presence
            'existing_website_url': forms.URLInput(attrs={'placeholder': 'http://yourexistingsite.com (Optional)', 'class': 'form-control'}),
            'social_media_links': forms.Textarea(attrs={'placeholder': 'e.g., https://facebook.com/yourpage\nhttps://instagram.com/yourprofile', 'rows': 3, 'class': 'form-control'}),

            # Target Audience & Competitors
            'target_audience_description': forms.Textarea(attrs={'placeholder': 'Who are you trying to reach?', 'rows': 3, 'class': 'form-control'}),
            'key_competitors': forms.Textarea(attrs={'placeholder': 'e.g., competitor1.com, example-site.com (I like their design)', 'rows': 3, 'class': 'form-control'}),

            'additional_comments': forms.Textarea(attrs={'placeholder': 'Anything else you\'d like to share?', 'rows': 3, 'class': 'form-control'}),
        }

        labels = {
            'business_description': 'Describe your Business/Organization',
            'services_offered': 'What are your key Services/Products?',
            'reason_online_presence': 'Establish an online presence',
            'reason_wider_audience': 'Reach a wider audience',
            'reason_leads_sales': 'Generate leads and sales',
            'reason_provide_info': 'Provide information to customers',
            'reason_brand_awareness': 'Build brand awareness',
            'reason_showcase_products': 'Showcase products/services',
            'reason_other': 'Other reason (Specify)',
            'main_goal_for_website': 'What are your main goals for the website?',
            'has_logo': 'Do you have a logo?',
            'has_brand_colors_fonts': 'Do you have brand colors and fonts?',
            'will_provide_content': 'Are you willing to provide all content (text, images)?',
            'willing_to_provide_testimonial': 'Willing to provide a testimonial if satisfied?',
            'existing_website_url': 'Existing Website URL (if any)',
            'social_media_links': 'Social Media Profile Links',
            'target_audience_description': 'Describe your Target Audience',
            'key_competitors': 'Key Competitors or Websites You Admire',
            'additional_comments': 'Additional Comments or Requirements',
        }

        help_texts = { # Add help texts directly in the form for more control if needed
            'main_goal_for_website': "Please list your goals in order of importance, or describe your top priority."
        }