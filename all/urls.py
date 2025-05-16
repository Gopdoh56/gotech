
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name ='home' ),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('free-website-campaign/', views.free_website_campaign_view, name='free_website_campaign'),
    path('free-website-campaign/success/', views.free_website_campaign_success_view, name='free_website_campaign_success')

]