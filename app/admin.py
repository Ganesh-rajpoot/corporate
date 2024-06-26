from django.contrib import admin
from .models import User,Mentor,ContactUs

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile', 'referral_code']
    search_fields = ['username', 'email', 'mobile']

    # Add more customization as needed


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'mobile_number', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email_id', 'mobile_number']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'message']
    search_fields = ['name', 'mobile', 'email', 'message']