from django.urls import path
from ..kggkHack import views  # Import views from the current app's views.py file

urlpatterns = [
    path('pages/', views.upload_to_s3, name=''),
]
