from django.urls import path
from . import views
from .views import DoctorListView

urlpatterns = [
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctor-list', DoctorListView.as_view(), name='doctor_list'),
]