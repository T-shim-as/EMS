from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # エンジニアかどうかを示すフラグ
    is_engineer = models.BooleanField(default=False)
    # 管理者かどうかを示すフラグ
    is_manager = models.BooleanField(default=False)
    # 電話番号（オプション）
    phone = models.CharField(max_length=15, blank=True, null=True)

class Engineer(models.Model):
    # UserモデルとEngineerモデルを1対1で関連付け
    # on_delete=models.CASCADEは、Userが削除されたらそれに関連するEngineerも削除される
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='engineer_profile')
    # 誕生日（オプション）
    birthday = models.DateField(null=True, blank=True)
    # 住所（オプション）
    address = models.TextField(blank=True)

    def __str__(self):
        # オブジェクトを文字列で表現するときはユーザー名を返す
        return self.user.username