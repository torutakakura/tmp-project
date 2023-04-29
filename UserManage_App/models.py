from django.db import models


# Create your models here.
class user(models.Model):
    
    # 項目の定義
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phone = models.IntegerField(blank=True, null=True)

