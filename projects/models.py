from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)  # プロジェクト名
    description = models.TextField()  # プロジェクトの説明
    start_date = models.DateField()  # プロジェクト開始日
    end_date = models.DateField(null=True, blank=True)  # プロジェクト終了日（オプション）
    time = models.TextField(null=True, blank=True)  # 勤務時間（オプション）
    address = models.TextField(null=True, blank=True)  # 勤務場所
    status = models.CharField(max_length=20, choices=[  # プロジェクトの状態
        ('proposal', '提案中'),
        ('ongoing', '進行中'),
        ('waiting', '結果待ち'),
        ('confirmed', '確定'),
        ('failure', '失敗'),
    ], default='proposal')

    def __str__(self):
        return self.name
    
    @property
    def status_choices(self):
        return self._meta.get_field('status').choices





# class ProjectAssignment(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE) # プロジェクトへの外部キー
#     engineer = models.ForeignKey('accounts.Engineer', on_delete=models.CASCADE) # エンジニアへの外部キー
#     role = models.CharField(max_length=100) # プロジェクトでの役割
#     start_date = models.DateField() # アサイン開始日
#     end_date = models.DateField(null=True, blank=True) # アサイン終了日（オプション）

#     class Meta:
#         unique_together = ('project', 'engineer') # プロジェクトとエンジニアの組み合わせはユニークであることを保証

#     def __str__(self):
#         return f"{self.engineer.user.username} on {self.project.name}"