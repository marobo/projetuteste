from django.urls import path, include
from appteste import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('posts', views.post_list, name="post_list"),
]