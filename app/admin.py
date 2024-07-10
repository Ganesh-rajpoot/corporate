from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile', 'referral_code']
    search_fields = ['username', 'email', 'mobile']

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'mobile_number', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email_id', 'mobile_number']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'message']
    search_fields = ['name', 'mobile', 'email', 'message']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # List the fields to display in the admin list view
    search_fields = ['title', 'content']  # Fields to search in the admin interface

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'salary', 'posted_at')
    list_filter = ('company_name', 'location', 'posted_at')
    search_fields = ('title', 'description', 'company_name')