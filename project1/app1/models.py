from django.db import models
from django.utils import timezone

class EventRecord(models.Model):
    name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    rfid = models.CharField(max_length=255, unique=True)  # Ensure rfid is unique

    def __str__(self):
        return f"{self.rfid}"

class Event_Log(models.Model):
    status = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    rfid = models.ForeignKey(EventRecord, on_delete=models.CASCADE)  # Foreign key to EventRecord

    def __str__(self):
        return f"{self.status}"
