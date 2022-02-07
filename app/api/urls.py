from django.urls import path
from app.api import views

urlpatterns = [
    path('stream/', views.stream_list, name="stream"),
    path('stream/<int:pk>', views.stream_details, name="stream_details"),
]
