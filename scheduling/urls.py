from django.urls import path
from .views import NewAppointmentView, AppointmentView

urlpatterns = [
    path('new-appointment/', NewAppointmentView.as_view(), name='new_appointment'),
    path('appointment/<int:pk>/', AppointmentView.as_view(), name='appointment'),
]