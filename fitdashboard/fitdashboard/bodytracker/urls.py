from django.urls import path
from bodytracker import views

urlpatterns = [
    path('index/', views.index, name='index'),
]