from django.utils import timezone
from rest_framework import serializers
from .models import EventRecord, Event_Log

class EventLogSerializer(serializers.Serializer):
    status = serializers.BooleanField(required=True)
    rfid = serializers.CharField(required=True)

    def validate_rfid(self, value):
        try:
            EventRecord.objects.get(rfid=value)
        except EventRecord.DoesNotExist:
            raise serializers.ValidationError("RFID does not exist.")
        return value

    def create(self, validated_data):
        rfid = validated_data.pop('rfid')
        event_record = EventRecord.objects.get(rfid=rfid)
        return Event_Log.objects.create(status=validated_data['status'], rfid=event_record)
    
    
from rest_framework import serializers
from .models import EventRecord, Event_Log

class EventDetailsSerializer(serializers.Serializer):
    rfid = serializers.CharField()
    name = serializers.CharField(read_only=True)
    event_name = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    time = serializers.DateTimeField(read_only=True)

    def validate_rfid(self, value):
        if not EventRecord.objects.filter(rfid=value).exists():
            raise serializers.ValidationError('RFID does not exist')
        return value

    def to_representation(self, instance):
        rfid = self.validated_data.get('rfid')
        event_record = EventRecord.objects.get(rfid=rfid)
        event_log = Event_Log.objects.filter(rfid=event_record).last()

        data = {
            'name': event_record.name,
            'event_name': event_record.event_name,
            'status': event_log.status if event_log else None,
            'time': event_log.time if event_log else None,
        }

        return data