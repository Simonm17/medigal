from django.urls import path
from . import views
from .views import DoctorListView, DoctorDetailView, DoctorUpdateView

urlpatterns = [
    path('add/', views.add_doctor, name='add_doctor'),
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
]