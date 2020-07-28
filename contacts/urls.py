from django.urls import path
from .views import AddressCreateView, AddressDetailView, AddressUpdateView, TelephoneCreateView, TelephoneUpdateView, EmailCreateView, EmailUpdateView

urlpatterns = [
    path('address/create/', AddressCreateView.as_view(), name='address_create'),
    path('address/<int:pk>/', AddressDetailView.as_view(), name='address_detail'),
    path('address/<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),

    path('telephone/create/', TelephoneCreateView.as_view(), name='telephone_create'),
    path('telephone/<int:pk>/update/', TelephoneUpdateView.as_view(), name='telephone_update'),

    path('email/create/', EmailCreateView.as_view(), name='email_create'),
    path('email/<int:pk>/update/', EmailUpdateView.as_view(), name='email_update'),
]