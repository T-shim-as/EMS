from django.shortcuts import render, get_object_or_404
from .models import Engineer

def engineer_list(request):
    engineers = Engineer.objects.all()
    return render(request, 'accounts/engineer_list.html', {'engineers': engineers})

def engineer_detail(request, pk):
    engineer = get_object_or_404(Engineer, pk=pk)
    return render(request, 'accounts/engineer_detail.html', {'engineer': engineer})