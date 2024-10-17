from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    # path('skills/', include('skills.urls')),
    # path('reports/', include('reports.urls')),
]