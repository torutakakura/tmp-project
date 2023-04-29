"""
URL configuration for UserManage_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Include関数をインポート
from django.urls import path,include


# path関数でUserManage_App内のurls.pyを読み込む、include関数を記述
urlpatterns = [
    path('admin/', admin.site.urls), #管理画面
    path('UserManage_App/', include('UserManage_App.urls')), #アプリケーションフォルダのurls.pyと関連付け
]
