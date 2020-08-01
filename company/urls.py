from django.urls import path
from .views import RequestCreateView

urlpatterns = [
    path('request/', RequestCreateView.as_view(), name='request_company'),
]