from django.urls import path
from .views import RequestCreateView, RequestListView

urlpatterns = [
    path('new-request/', RequestCreateView.as_view(), name='request_company'),
    path('requests/', RequestListView.as_view(), name='request_list'),
]