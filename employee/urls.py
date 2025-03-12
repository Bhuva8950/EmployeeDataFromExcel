from django.urls import path
from .views import AddDataView

urlpatterns = [
    path('add_data/', AddDataView.as_view(), name='upload-excel'),
] 