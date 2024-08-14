
from django.shortcuts import render, redirect
from .models import EventRecord
from .forms import EventRecordForm

def add_event_record(request):
    if request.method == 'POST':
        form = EventRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_records')  # Redirect to the page showing the updated list
    else:
        form = EventRecordForm()

    # Render the template with the form and the records
    records = EventRecord.objects.all()
    return render(request, 'app1/add_event_records.html', {
        'form': form,
        'records': records,
        'form_errors': form.errors.as_data() if form.errors else None
    })
    
    

def show_event_records(request):
    records = EventRecord.objects.all()
    return render(request, 'app1/event_records.html', {'records': records})



def event_log_view(request):
    # Fetch all EventRecord objects
    records = EventRecord.objects.all()
    
    # Optionally, you can include related Event_Log objects
    # This will allow you to access event logs directly from each EventRecord
    records = EventRecord.objects.prefetch_related('event_log_set')
    
    # Render the template with the records
    return render(request, 'app1/event_log.html', {'records': records})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventLogSerializer,EventDetailsSerializer

class EventLogCreateView(APIView):
    def post(self, request):
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventRecord, Event_Log
import json

class EventDetailsView(APIView):
    def get(self, request):
        # Try to read rfid from request body (assuming it's in JSON format)
        try:
            body = json.loads(request.body.decode('utf-8'))
            rfid = body.get('rfid')
        except (json.JSONDecodeError, AttributeError):
            return Response({'error': 'Invalid JSON format or missing RFID'}, status=status.HTTP_400_BAD_REQUEST)

        if not rfid:
            return Response({'error': 'RFID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            event_record = EventRecord.objects.get(rfid=rfid)
        except EventRecord.DoesNotExist:
            return Response({'error': 'RFID does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Get the latest Event_Log for the given RFID
        event_log = Event_Log.objects.filter(rfid=event_record).last()

        # Prepare the response data
        response_data = {
            'name': event_record.name,
            'event_name': event_record.event_name,
            'status': event_log.status if event_log else None,
            'time': event_log.time if event_log else None,
        }

        return Response(response_data)
    
def aaa(request):
    return render(request,'app1/index.html')