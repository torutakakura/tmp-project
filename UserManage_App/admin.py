from django.contrib import admin

# Register your models here.
# モデルをインポート
from . models import user

# 管理ツールに登録
admin.site.register(user)