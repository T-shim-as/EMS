from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # ユーザー作成フォームをカスタムフォームに設定
    form = CustomUserChangeForm  # ユーザー編集フォームをカスタムフォームに設定
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']  # 管理画面のリスト表示項目
    
    # ユーザー詳細画面のフィールドセット
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'role')}),  # 追加フィールドを表示
    )
    # ユーザー追加画面のフィールドセット
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'role')}),  # 追加フィールドを表示
    )

    def has_add_permission(self, request):
        # スーパーユーザー（管理者）のみがユーザーを追加できるように制限
        return request.user.is_superuser

admin.site.register(CustomUser, CustomUserAdmin)  # カスタムユーザーモデルを管理画面に登録