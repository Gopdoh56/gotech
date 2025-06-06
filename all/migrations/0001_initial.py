# Generated by Django 5.1.5 on 2025-05-16 07:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeWebsiteSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('project_name_or_idea', models.CharField(help_text='Name of your existing business, project, or a brief idea.', max_length=255)),
                ('project_description', models.TextField(help_text='Tell us a bit more about your project and why you need a website.')),
                ('existing_website_url', models.URLField(blank=True, help_text='If you have an existing website, please share the link.', null=True)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('contacted_for_website', models.BooleanField(default=False, help_text="Check this if you've contacted them about the free website.")),
                ('website_built', models.BooleanField(default=False, help_text='Check this if the free website has been built.')),
            ],
            options={
                'verbose_name': 'Free Website Submission',
                'verbose_name_plural': 'Free Website Submissions',
                'ordering': ['-submission_date'],
            },
        ),
    ]
