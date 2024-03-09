from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext,gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ( 'avatar', 'phone_number', 'region')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Product)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Size_category)
admin.site.register(Card)
admin.site.register(Saved)
admin.site.register(Office)
admin.site.register(Order)
