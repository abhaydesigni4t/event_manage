
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