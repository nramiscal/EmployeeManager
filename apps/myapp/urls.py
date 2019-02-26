from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('manager/<manager_id>', views.manager),
]
