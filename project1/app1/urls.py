from django.urls import path
from app1 import views
#from .views import 



urlpatterns = [
    
    path('', views.show_event_records, name='event_records'),
    path('add_event/',views.add_event_record,name='add_event'),
    path('event_log/', views.event_log_view, name='event_log'),
 
    
]