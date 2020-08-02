from django.urls import path
from . import views
from .views import Get404View

urlpatterns = [
    path('', views.home, name='index-home'),
    path('404/', Get404View.as_view(), name='index-404'),
]