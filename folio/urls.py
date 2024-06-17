
from django.urls import path
from .views import PortView

urlpatterns = [
    path('', PortView, name='portfolio'),
]
