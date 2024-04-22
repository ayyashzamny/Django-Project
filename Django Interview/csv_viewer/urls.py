# yourapp/urls.py

from django.urls import path
from . import views
from .views import visualize_data

urlpatterns = [
    path('', views.import_csv, name='import-csv'),
    path('visualize/', visualize_data, name='visualize-data'),
]
