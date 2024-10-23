from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # AbstractUserから継承されるフィールド：
    # username = models.CharField(max_length=150, unique=True) 
    # first_name = models.CharField(max_length=150, blank=True)
    # last_name = models.CharField(max_length=150, blank=True)
    # email = models.EmailField(blank=True)
    # password = models.CharField(max_length=128)

    # ユーザーの役職を定義
    ROLE_CHOICES = (
        ('engineer', 'エンジニア'),
        ('engineer_manager', 'エンジニアマネージャー'),
        ('hr', '人事'),
        ('sales', '営業'),
        ('admin', '管理者'),
    )
    # 追加のフィールドを定義
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')

    # 管理画面などでの表示名をユーザー名に設定
    def __str__(self):
        return self.username