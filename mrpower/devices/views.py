from django.shortcuts import render
from .models import Device

def device_list(request):
    devices = Device.objects.all().order_by('-created_at')
    return render(request, 'devices/device_list.html', {
        'devices': devices
    })


from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)

    # Device health check
    is_online = False
    if device.last_seen:
        is_online = timezone.now() - device.last_seen < timedelta(minutes=5)

    return render(request, 'devices/device_detail.html', {
        'device': device,
        'is_online': is_online
    })
