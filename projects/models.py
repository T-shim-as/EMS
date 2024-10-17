from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    name = models.CharField(max_length=200)  # プロジェクト名
    description = models.TextField()  # プロジェクトの説明
    must_skill = models.CharField(max_length=200, null=True, blank=True)  # 必須スキル（オプション） 
    better_skill = models.CharField(max_length=200, null=True, blank=True)  # 尚可スキル（オプション） 
    start_date = models.DateField()  # プロジェクト開始日
    end_date = models.DateField(null=True, blank=True)  # プロジェクト終了日（オプション）
    work_time = models.CharField(max_length=200, null=True, blank=True)  # 勤務時間（オプション）
    address = models.CharField(max_length=200, null=True, blank=True)  # 勤務場所
    status = models.CharField(max_length=20, choices=[  # プロジェクトの状態
        ('proposal', '提案'),
        ('ongoing', '進行中'),
        ('interview', '面談'),
        ('waiting', '結果待ち'),
        ('join', '確定'),
    ], default='proposal')

    # 案件合致度（業務内容）
    content_match = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True,
        verbose_name="業務内容合致度"
    )

    # 案件合致度（就業環境）
    environment_match = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True,
        verbose_name="就業環境合致度"
    )

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