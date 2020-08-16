from django.urls import path

from .views import NewAppointmentView, AppointmentView, AppointmentListView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
    path('new-appointment/', NewAppointmentView.as_view(), name='new_appointment'),
    path('appointment/<int:pk>/', AppointmentView.as_view(), name='appointment'),
]