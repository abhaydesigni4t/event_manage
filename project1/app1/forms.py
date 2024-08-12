from django import forms
from .models import EventRecord, Event_Log

class EventRecordForm(forms.ModelForm):
    class Meta:
        model = EventRecord
        fields = ['name', 'event_name', 'rfid']
    
    def clean_rfid(self):
        rfid = self.cleaned_data.get('rfid')
        if EventRecord.objects.filter(rfid=rfid).exists():
            raise forms.ValidationError("Data with this RFID already exists.")
        return rfid

class EventLogForm(forms.ModelForm):
    class Meta:
        model = Event_Log
        fields = '__all__'
        
        