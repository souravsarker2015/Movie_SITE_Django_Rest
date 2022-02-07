from django.urls import path
from app.api import views

urlpatterns = [
    path('stream/', views.stream_list, name="stream"),
]
