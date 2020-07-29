from django.urls import path
from .views import AddressCreateView, AddressUpdateView, AddressDeleteView, TelephoneCreateView, TelephoneUpdateView, TelephoneDeleteView, EmailCreateView, EmailUpdateView, EmailDeleteView

urlpatterns = [
    path('address/create/', AddressCreateView.as_view(), name='address_create'),
    path('address/<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),
    path('address/<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),

    path('telephone/create/', TelephoneCreateView.as_view(), name='telephone_create'),
    path('telephone/<int:pk>/update/', TelephoneUpdateView.as_view(), name='telephone_update'),
    path('telephone/<int:pk>/delete/', TelephoneDeleteView.as_view(), name='telephone_delete'),

    path('email/create/', EmailCreateView.as_view(), name='email_create'),
    path('email/<int:pk>/update/', EmailUpdateView.as_view(), name='email_update'),
    path('email/<int:pk>/delete/', EmailDeleteView.as_view(), name='email_delete'),
]