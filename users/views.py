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
            response.set_signed_cookie("login", "yes", salt='SSS', max_age=60 * 60)
            return response
        else:
            messages.success(request, "密码错误")
            return render(request, "login.html")

    elif request.method == "GET":
        return render(request, "login.html")


def logout(request):
    rep = redirect("/user/login/")
    # 删除用户浏览器上之前设置的cookie
    rep.delete_cookie('login')
    return rep

def check_login(func):
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        # 假设设置的cookie的key为login，value为yes
        if request.get_signed_cookie("login", salt="SSS", default=None) == 'yes':
            # 已经登录的用户，则放行
            return func(request, *args, **kwargs)
        else:
            # 没有登录的用户，跳转到登录页面
            return redirect(f"/users/login?next={next_url}")

    return inner

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



def page_not_found(request,exception):
    return render(request,'404.html')