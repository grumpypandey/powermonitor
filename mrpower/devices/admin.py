from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'location', 'is_active', 'last_seen')
    list_filter = ('device_type', 'is_active')
    search_fields = ('name', 'location')
