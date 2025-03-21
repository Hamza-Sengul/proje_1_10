from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from. models import Customer
from .models import User

admin.site.register(Customer)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active')

from .models import AdminProfile

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')