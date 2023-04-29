from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import user
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

# ユーザー追加ページ
def user_add(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            try:
                new_user = form.save()
                messages.success(request,'ユーザ追加に成功しました！！')
                return redirect(reverse('myapp:user_list'))
            except:
                messages.error(request,'ユーザ追加に失敗しました！！')
    else:
        form = TaskForm()
    
    return render(request, 'add_user.html', {'form': form})

# トップページ 
def user_list(request):
    user_list = user.objects.all()
    return render(request, 'index.html', {'user_list': user_list, })


# アップデートページ
def user_detail(request, pk):
    object = get_object_or_404(user, pk=pk)
    one_user = user.objects.filter(id=pk)[0]
    print(object)
    print(one_user)

    return render(request, 'update_user.html', {'object': object, })

def user_update(request, pk):
    target_user = get_object_or_404(user, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=target_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'ユーザ情報を更新しました！！')
            return redirect(reverse('myapp:user_list'))
        else:
            messages.error(request, 'ユーザ情報の更新に失敗しました！！')
    else:
        form = TaskForm(instance=target_user)
    
    return render(request, 'myapp/index.html', {'form': form, 'object': target_user})

# def user_update(request, pk):
    # target_user = get_object_or_404(user, pk=pk)
    # target_user.Name= request.POST.get("name")
    # target_user.Email= request.POST.get("email")
    # target_user.Phone= request.POST.get("phone")
    # target_user.save()
    # messages.success(request, ('ユーザ情報を更新しました！！'))

    # return render(request, 'index.html', {'form': TaskForm, 'object': target_user })

# ユーザー削除
def user_delete(requset, pk):
    object = get_object_or_404(user, pk=pk)
    
    object.delete()
    return redirect(reverse('myapp:user_list'))

