from django.urls import path, include
from appteste import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('create', views.post_create, name="post_create"),
    path('posts', views.post_list, name="post_list"),
]