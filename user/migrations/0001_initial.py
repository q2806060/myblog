# Generated by Django 2.1.8 on 2019-10-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginname', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=40)),
                ('uemail', models.EmailField(max_length=254, null=True)),
                ('telPhone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('idCard', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.IntegerField(choices=[(1, '男'), (0, '女')], default=1)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('loginCount', models.IntegerField(default=0)),
                ('birthday', models.DateField(null=True)),
                ('wechat', models.CharField(max_length=30, null=True)),
                ('qq', models.CharField(max_length=15, null=True)),
                ('balance', models.FloatField(default=0)),
            ],
        ),
    ]
