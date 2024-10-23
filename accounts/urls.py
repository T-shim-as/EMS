from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views  # あなたのビューをインポート

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),  # /accounts/ を /accounts/login/ にリダイレクト
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 他のアカウント関連のURLパターン
]