from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return  render(request, 'home.html',)

def about(request):
    return render(request, 'about.html')

def academics(request):
    return render(request, 'academics.html')


def admissions(request):
    return render(request, 'admissions.html')


# landing_page/views.py
from django.shortcuts import render, redirect
from django.contrib import messages # For displaying success/error messages
from .forms import FreeWebsiteForm
from .models import FreeWebsiteSubmission # If you need to query existing submissions

# ... your existing home_page view ...

def free_website_campaign_view(request):
    if request.method == 'POST':
        form = FreeWebsiteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thank you! Your submission for a free website has been received. We will review it and get in touch if selected.')
                return redirect('free_website_campaign_success') # Redirect to a success page or back to the form page
            except Exception as e: # Catch potential unique constraint errors etc.
                # Check if it's a unique constraint violation for email
                if 'UNIQUE constraint failed: landing_page_freewebsitesubmission.email' in str(e):
                     messages.error(request, 'This email address has already been submitted. Please use a different email.')
                else:
                    messages.error(request, f'An error occurred: {e}. Please try again.')
                # Optionally, log the full error e for debugging
    else:
        form = FreeWebsiteForm()

    # Count existing submissions to display on the page if you want
    submission_count = FreeWebsiteSubmission.objects.count()
    remaining_spots = max(0, 50 - submission_count) # Assuming 50 free websites

    context = {
        'form': form,
        'submission_count': submission_count,
        'remaining_spots': remaining_spots,
        'page_title': "Apply for a Free Website!",
        'campaign_description': "GOtech Solutions is offering 50 free websites to help businesses and individuals get online! Fill out the form below to apply."
    }
    return render(request, 'free_website_form.html', context)

def free_website_campaign_success_view(request):
    # You might not have this view if you redirect back to the form page with a message
    # But if you want a dedicated success page:
    return render(request, 'free_website_success.html')