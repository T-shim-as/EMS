from django.urls import path
from .views import EngineerListView

urlpatterns = [
    path('engineers/', EngineerListView.as_view(), name='engineer_list'),
]