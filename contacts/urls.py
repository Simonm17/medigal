from django.urls import path
from .views import AddressUpdateView

urlpatterns = [
    path('address-detail/<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),
]