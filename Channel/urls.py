from django.urls import path
from Channel import views

urlpatterns = [
    path('push/es/', views.push_to_es),
]
