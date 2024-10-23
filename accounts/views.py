from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProjectListView(ListView):
    # ...

@login_required
def update_project_status(request, pk):