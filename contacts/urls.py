from django.urls import path
from .views import AddressDetailView, AddressUpdateView

urlpatterns = [
    path('<int:pk>/', AddressDetailView.as_view(), name='address_detail'),
    path('<int:pk>/update/', AddressUpdateView.as_view(), name='address_update'),
]