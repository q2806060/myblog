from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.hashers import make_password, check_password
# 用于序列化查询结果 srlz("json", user.objects.all())
from django.core.serializers import serialize as srlz
from .models import *

# Create your views here.

def sendResult(msg=None):
    retmsg = {}
    if msg:
        if "error_code" in msg:
            retmsg["error_code"] = msg["error_code"]
            msg.pop("error_code")
            msg = json.loads(srlz("json", msg))
            retmsg["data"] = msg
        else:
            retmsg["error_code"] = 0
            msg = json.loads(srlz("json", msg))
            retmsg["data"] = msg
    else:
        retmsg["error_code"] = 0
        retmsg["data"] = {}
    
    return JsonResponse(retmsg)

def _checkLogin(request):
    if request.session.get("loginname", '') and request.session.get("password"):
        try:
            name = request.session["loginname"]
            pwd = request.session["password"]
            user = User.objects.get(loginname=name)
            if pwd == user.password:
                return user
            else:
                return False
        except:
            return False
    else:
        return False


class Users:
    @staticmethod
    def login_view(request):
        if request.method == "GET":
            if _checkLogin(request):
                return redirect("/")
            return render(request, "index.html")
        else:
            loginname = request.POST.get('loginname', '')
            password = request.POST.get('password', '')
            if loginname and password:
                try:
                    user = User.objects.get(loginname=loginname)
                    ret = check_password(password, user.password)
                    if user and ret:
                        request.session['loginname'] = loginname
                        request.session['password'] = user.password
                        data = {

                        }
                        return sendResult(data)
                    else:
                        data = {
                            "error_code" : 104,
                            'error_msg':'账号或密码错误！',
                        }
                        return sendResult(data)
                except:
                    data = {
                        "error_code" : 104,
                        "error_msg":"账号或密码错误！"
                    }
                    return sendResult(data)
            else:
                data = {
                    "error_code" : 103,
                    'error_msg':'请输入完整信息'
                }
                return sendResult(data)

    @staticmethod
    def register_view(request):
        if request.method == "GET":
            return render(request, "index.html")
        else:
            loginname = request.POST.get('loginname', '')
            username = request.POST.get('username', '')
            password = request.POST.get('loginpwd', '')
            telphone = request.POST.get('telphone', '')
            if loginname and password and telphone:
                user = User.objects.filter(loginname=loginname)
                if user:
                    data = {
                        "error_code" : 101,
                        "error_msg" : "用户名重复",
                    }
                    
                    return sendResult(data)
                else:
                    password = make_password(password, None, 'pbkdf2_sha1')
                    User.objects.create(
                        loginname = loginname,
                        username = username,
                        password = password,
                        telPhone = telphone
                    )
                    request.session['loginname'] = loginname
                    request.session['password'] = password
                    data = {
                        "msg" : "注册成功，即将跳转页面",
                    }
                    return sendResult(data)
            else:
                data = {
                    "error_code" : 110,
                    'error_msg':"请重新注册或联系管理员"
                }
                return sendResult(data)

    @staticmethod
    def logout_view(request):
        request.session.flush()
        return sendResult()

