from django.urls import path
from .views import AddressDetailView, AddressUpdateView, TelephoneUpdateView, EmailUpdateView

urlpatterns = [
    path('address/<int:pk>/', AddressDetailView.as_view(), name='address_detail'),
    path('address/<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),
    path('telephone/<int:pk>/update/', TelephoneUpdateView.as_view(), name='telephone_update'),
    path('email/<int:pk>/update/', EmailUpdateView.as_view(), name='email_update'),
]