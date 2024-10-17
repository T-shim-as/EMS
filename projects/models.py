from django.db import models

class Project(models.Model):
    # プロジェクト名
    name = models.CharField(max_length=200)
    # プロジェクトの説明
    description = models.TextField()
    # プロジェクト開始日
    start_date = models.DateField()
    # プロジェクト終了日（オプション）
    end_date = models.DateField(null=True, blank=True)
    # プロジェクトの状態
    status = models.CharField(max_length=20, choices=[
        ('planning', 'Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold')
    ])
    # プロジェクトに割り当てられたエンジニア（多対多の関係）
    engineers = models.ManyToManyField('accounts.Engineer', through='ProjectAssignment')

    def __str__(self):
        return self.name

class ProjectAssignment(models.Model):
    # プロジェクトへの外部キー
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # エンジニアへの外部キー
    engineer = models.ForeignKey('accounts.Engineer', on_delete=models.CASCADE)
    # プロジェクトでの役割
    role = models.CharField(max_length=100)
    # アサイン開始日
    start_date = models.DateField()
    # アサイン終了日（オプション）
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        # プロジェクトとエンジニアの組み合わせはユニークであることを保証
        unique_together = ('project', 'engineer')

    def __str__(self):
        return f"{self.engineer.user.username} on {self.project.name}"