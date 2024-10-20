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
            'project_period',
            'work_time',
            'address',
            'is_telework',
            'status',
            ]
        widgets = {
            'is_telework': forms.CheckboxInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name':'案件名',
            'description':'案件詳細',
            'must_skill':'必須スキル',
            'better_skill':'尚可スキル',
            'project_period':'業務期間',
            'work_time':'勤務時間',
            'address':'勤務地',
            'is_telework':'テレワーク有',
            'status':'状態',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # 新規作成の場合
            self.fields['status'].initial = 'proposal'

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['status']