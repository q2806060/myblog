from django.db import models

# Create your models here.



class User(models.Model):
    loginname = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=60)
    uemail = models.EmailField(null=True)
    telPhone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    idCard = models.CharField(max_length=20, blank=True,null=True)
    sex = models.IntegerField(choices=((1,'男'),(0,'女')),default=1)
    address = models.CharField(max_length=150, null=True, blank=True)
    loginCount = models.IntegerField(default=0)
    birthday = models.DateField(null=True)
    wechat = models.CharField(max_length=30, null=True)
    qq = models.CharField(max_length=15, null=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        if not self.username:
            return self.loginname
        else:
            return self.username

    class Mate:
        db_table = 'userinfo'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name