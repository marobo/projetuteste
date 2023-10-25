from django.urls import path, include
from appteste import views

urlpatterns = [
    path('', views.index, name="homepage")
]