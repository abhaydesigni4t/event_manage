from django.urls import path
from app1 import views
from .views import EventLogCreateView,EventDetailsView



urlpatterns = [
    
    path('', views.show_event_records, name='event_records'),
    path('add_event/',views.add_event_record,name='add_event'),
    path('event_log/', views.event_log_view, name='event_log'),
    path('event_log_api/', EventLogCreateView.as_view(), name='event_log_create'),
    path('event_details/', EventDetailsView.as_view(), name='event_details'),
    path('aaa/', views.aaa, name='aaa'),

 
    
]