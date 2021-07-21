import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect
from users import models
# Create your views here.
def login(request):
    user = models.user()
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        print(name)
        print(pwd)
        try:
            user = models.user.objects.get(name=name)
        except Exception as e:
            print(e)
            messages.success(request, "用户名错误")
            return render(request, "login.html")
        if user.password==pwd:
            response = redirect('/show/test3/')

            response.set_signed_cookie("id", user.id, salt="yzh", max_age=60 * 60)
            response.set_signed_cookie("name", user.name, salt="yzh", max_age=60 * 60)
            response.set_signed_cookie("pwd", user.password, salt="yzh", max_age=60 * 60)
            return response
        else:
            messages.success(request, "密码错误")
            return render(request, "login.html")
    elif request.method == "GET":
        return render(request, "login.html")


def logout(request):
    rep = redirect("/users/login/")
    # 删除用户浏览器上之前设置的cookie
    rep.delete_cookie('id')
    rep.delete_cookie('name')
    rep.delete_cookie('pwd')
    return rep



def register(request):
    user = models.user()
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.password = request.POST.get("password")
        againpwd = request.POST.get("password2")
        if againpwd!=user.password:
            messages.success(request, "两次密码不一致")
            return render(request, "register.html")
        if models.user.objects.filter(name=user.name).exists() == False:
            user.save()
            return render(request, "login.html")
        else:
            messages.success(request, "用户存在")
            return render(request, "register.html")
    elif request.method == "GET":
        return render(request, "register.html")

@csrf_exempt
def setinfo(request):
    user_id = request.get_signed_cookie('id', salt='yzh')
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        againpwd = data["repassword"]
        rsp = {"code": 200, "msg": "cg", "count": 1, "status":''}
        if models.user.objects.filter(name=data["username"]).exists() == True and str(user_id)!=str(models.user.objects.get(name=data["username"]).id):
            rsp["status"] = 201
            rsp["msg"] = "用户名重复"
        elif againpwd!=data["password"]:
            rsp["status"] = 201
            rsp["msg"] = "两次密码不同"
        else:
            rsp["status"] = 200
            rsp["msg"] = "cg"
            models.user.objects.filter(id=user_id).update(name = data["username"], password = data["password"])
        return HttpResponse(json.dumps(rsp), content_type="application/json")

    elif request.method == "GET":
        return render(request, "setinfo.html")


# 装饰器
def check_login(func):
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        # 假设设置的cookie的key为login，value为yes
        try:
            id = request.get_signed_cookie('id',salt='yzh')
            login_username = request.get_signed_cookie('name',salt='yzh')
            login_password = request.get_signed_cookie('pwd',salt='yzh')
        except Exception as e:
            return redirect(f"/users/login?next={next_url}")
        # 获取登录用户信息
        login_user = models.user.objects.get(name=login_username, password=login_password)

        # 返回登录成功后页面
        if str(login_user.id) == str(id):
            # 已经登录的用户，则放行
            return func(request, *args, **kwargs)
        else:
            # 没有登录的用户，跳转到登录页面
            return redirect(f"/users/login?next={next_url}")

    return inner

def page_not_found(request,exception):
    return render(request,'404.html')