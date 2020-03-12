from django.shortcuts import render
from .models import *
from user.views import _checkLogin, sendResult
from datetime import datetime

# Create your views here.


def get_timeaxis(request):
    if request.method == "GET":
        ret = TimeAxis.objects.all()
        return sendResult(ret)
    else:
        title = request.POST.get("title", '')
        content = request.POST.get("content", '')
        pubtime = datetime.now().strftime("%Y-%m-%d")
        if title and content:
            TimeAxis.objects.create(
                title = title,
                content = content,
                pubtime = pubtime,
            )
            data = {
                "msg" : "添加成功"
            }
            return sendResult(data)
        else:
            data = {
                "error_code" : 102,
                "error_msg" : "请输入内容"
            }
            return sendResult(data)