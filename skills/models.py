from django.db import models

class Skill(models.Model):
    # スキルの名前
    name = models.CharField(max_length=100)
    # スキルの説明（オプション）
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class EngineerSkill(models.Model):
    # Engineerモデルへの外部キー
    engineer = models.ForeignKey('accounts.Engineer', on_delete=models.CASCADE)
    # Skillモデルへの外部キー
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    # スキルの熟練度（1から5の整数）
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        # エンジニアとスキルの組み合わせはユニークであることを保証
        unique_together = ('engineer', 'skill')

    def __str__(self):
        return f"{self.engineer.user.username} - {self.skill.name} (Level: {self.proficiency})"