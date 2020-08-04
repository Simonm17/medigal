from django.urls import path
from .views import RequestCreateView, RequestListView, RequestDetailView, RequestUpdateView, CompanyCreateView

urlpatterns = [
    path('new-request/', RequestCreateView.as_view(), name='request_company'),
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('requests/<int:pk>/update/', RequestUpdateView.as_view(), name='request_update'),
    path('create-company/', CompanyCreateView.as_view(), name='create_company'),
]