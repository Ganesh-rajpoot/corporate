from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile', 'referral_code']
    search_fields = ['username', 'email', 'mobile']
    # Add more customization as needed
