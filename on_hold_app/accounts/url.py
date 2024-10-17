from django.urls import path
from . import views

urlpatterns = [
    path('engineers/', views.engineer_list, name='engineer_list'),
    path('engineers/<int:pk>/', views.engineer_detail, name='engineer_detail'),
]