from django.db import models

class Device(models.Model):
    DEVICE_TYPE_CHOICES = (
        ('ESP8266', 'ESP8266'),
        ('ESP32', 'ESP32'),
        ('SIM', 'Simulator'),
    )

    name = models.CharField(max_length=100)
    device_type = models.CharField(
        max_length=10,
        choices=DEVICE_TYPE_CHOICES,
        default='SIM'
    )

    location = models.CharField(
        max_length=150,
        help_text="Physical location (hostel, room, pole number, etc.)"
    )

    is_active = models.BooleanField(default=True)

    last_seen = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Last time the device sent data"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.device_type})"
