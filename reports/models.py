from django.db import models

class DailyReport(models.Model):
    # レポートを書いたエンジニアへの外部キー
    engineer = models.ForeignKey('accounts.Engineer', on_delete=models.CASCADE)
    # レポートの日付
    date = models.DateField()
    # レポートの内容
    content = models.TextField()
    # 稼働時間（小数点2桁まで）
    hours_worked = models.DecimalField(max_digits=4, decimal_places=2)
    # 関連するプロジェクト（オプション）
    # SET_NULLは、プロジェクトが削除されてもレポートは残す
    project = models.ForeignKey('projects.Project', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        # エンジニアと日付の組み合わせはユニークであることを保証（1日1レポート）
        unique_together = ('engineer', 'date')

    def __str__(self):
        return f"{self.engineer.user.username}'s report on {self.date}"