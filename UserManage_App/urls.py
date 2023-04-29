# path関数をインポート
from django.urls import path, re_path
# views.pyをインポート
from . import views

app_name = 'myapp'

# path関数(アドレスと呼び出し処理)
urlpatterns = [
    path('', views.user_list, name='user_list'), #127.0.0.1:8000/myapp
    path('user_form/', views.user_add, name='user_add'),  #127.0.0.1:8000/myapp/user_form/
    path(r'<int:pk>/', views.user_detail, name='user_detail'), #127.0.0.1:8000/myapp/<ID>/
    path(r'<int:pk>/update/', views.user_update, name='user_update'), #127.0.0.1:8000/myapp/<ID>/update/
    path(r'<int:pk>/delete/', views.user_delete, name='user_delete'), #127.0.0.1:8000/myapp/<ID>/delete/
    ]