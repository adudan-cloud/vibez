from django.contrib import admin
from .models import User  # Import User model

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')  # Ensure 'phone' exists in User model

admin.site.register(User, CustomUserAdmin)

