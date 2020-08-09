from django.urls import path
from . import views
from .views import DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorPreferenceView, DoctorNoteView

urlpatterns = [
    path('add/', views.add_doctor, name='add_doctor'),
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('<int:pk>/preferences/', DoctorPreferenceView.as_view(), name='doctor_preference'),
    path('<int:pk>/notes/', DoctorNoteView.as_view(), name='doctor_notes'),
]