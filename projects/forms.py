from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'must_skill',
            'better_skill',
            'start_date',
            'end_date',
            'work_time',
            'address',
            'status'
            ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # 新規作成の場合
            self.fields['status'].initial = 'proposal'

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['status']