from django.urls import path
from . import views
from .views import DoctorListView, DoctorDetailView, DoctorUpdateView

urlpatterns = [
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctor-list/', DoctorListView.as_view(), name='doctor_list'),
    path('doctor-detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor-detail/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
]