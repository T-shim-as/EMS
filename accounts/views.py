from django.views.generic import ListView
from .models import Engineer

class EngineerListView(ListView):
    model = Engineer
    template_name = 'accounts/engineer_list.html'
    context_object_name = 'engineers'