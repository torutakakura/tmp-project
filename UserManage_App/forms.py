#-*- coding:utf-8 -*-
from .models import user
from django import forms

class TaskForm(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # phone = forms.IntegerField()

    class Meta:
        model = user
        fields = "__all__"
