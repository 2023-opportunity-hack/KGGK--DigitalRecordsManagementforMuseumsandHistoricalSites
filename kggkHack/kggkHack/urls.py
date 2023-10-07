from django.urls import path, include  # new
from .views import upload_to_s3

urlpatterns = [
    
    path('', upload_to_s3, name=''),
]
