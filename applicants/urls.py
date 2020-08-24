from django.urls import path

from .views import (
    ApplicantCreateView,
    ApplicantListView,
    ApplicantDetailView,
    ApplicantUpdateView,
    ApplicantNoteView,
)

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant_list'),
    path('add-applicant', ApplicantCreateView.as_view(), name='add_applicant'),
    path('<int:pk>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('<int:pk>/update/', ApplicantUpdateView.as_view(), name='applicant_update'),
    path('<int:pk>/notes/', ApplicantNoteView.as_view(), name='applicant_notes'),   
]