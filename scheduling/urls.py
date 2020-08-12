from django.urls import path
from .views import NewAppointmentView

urlpatterns = [
    path('new-appointment/', NewAppointmentView.as_view(), name='new_appointment'),
    
]