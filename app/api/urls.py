from django.urls import path
from app.api import views

urlpatterns = [
    path('stream/', views.stream_list, name="stream"),
    path('stream/<int:pk>/', views.stream_details, name="stream_details"),
    path('list/', views.WatchListAV.as_view(), name="list"),
    path('<int:pk>/', views.WatchListDetailAV.as_view(), name="watchlist_details"),
    path('<int:pk>/review_create/', views.review_create, name="review_create"),
    path('<int:pk>/review/', views.ReviewList.as_view(), name="review"),

    path('review/<int:pk>/', views.ReviewDetails.as_view(), name="review_details"),
]
