from django.db import models

# Create your models here.

class TimeAxis(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pubtime = models.DateField()

    class Mate:
        db_table = "timeaxis"
        verbose_name = "时间轴"
        verbose_name_plural = verbose_name