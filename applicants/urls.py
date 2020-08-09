from django.urls import path
from . import views
from .views import ApplicantListView, ApplicantDetailView, ApplicantUpdateView, ApplicantNoteView

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant_list'),
    path('add-applicant', views.add_applicant, name='add_applicant'),
    path('<int:pk>/', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('<int:pk>/update/', ApplicantUpdateView.as_view(), name='applicant_update'),
    path('<int:pk>/notes/', ApplicantNoteView.as_view(), name='applicant_notes'),
    
]