from django.urls import path
from .views import RequestCreateView, RequestListView, CompanyCreateView

urlpatterns = [
    path('new-request/', RequestCreateView.as_view(), name='request_company'),
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('create-company', CompanyCreateView.as_view(), name='create_company'),
]