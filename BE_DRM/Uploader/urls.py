from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.upload_to_s3, name='upload'),
]
