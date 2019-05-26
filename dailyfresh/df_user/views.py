from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from hashlib import sha1  # 加密用
from .models import *
from . import user_decorator
from df_goods import models as dfg
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handel(request):
    post = request.POST
    # 接受用户输入
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否一致
    if upwd != upwd2:
        data = '两次密码不一致'
        return redirect('/user/register/', {'data': data})
    # 密码加密
    s = sha1()
    s.update(upwd.encode())
    upwd3 = s.hexdigest()
    # 存入数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    # print(count)
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登录',
        'error_name': 0,
        'error_pwd': 0,
        'uname': uname}
    return render(request, 'df_user/login.html', context)


def login_handel(request):
    # 接受请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)  # 勾选为1 不勾选为0
    # 根据用户名查询数据
    user = UserInfo.objects.filter(uname=uname)  # filter查不到返回[]get查不到抛异常
    # print(uname)
    # 判断：如果未查询到则用户名错误，如果查到则判断密码是否正确，正确则转向用户中心
    if len(user) == 1:  # 用户名存在
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == user[0].upwd:
            # url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect('/')
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return red
        else:  # 密码错误
            context = {
                'title': '用户登录',
                'error_name': 0,
                'error_pwd': 1,
                'uname': uname,
                'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:  # 用户名不存在
        context = {
            'title': '用户登录',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd}
        return render(request, 'df_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')


@user_decorator.login
def info(request):
    # uname = request.session.get['user_name']
    uemail = UserInfo.objects.get(id=request.session['user_id']).uemail
    # 读取cookie信息得到最近浏览
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(",")
    goods_list = []
    for goods_id in goods_ids1:
        try:
            goods_list.append(dfg.GoodsInfo.objects.get(id=int(goods_id)))
        except BaseException:
            pass
    context = {
        'title': '用户中心',
        'uname': request.session['user_name'],
        "email": uemail,
        'good_list': goods_list,
    }
    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    # print(user)
    if request.method == 'POST':
        post = request.POST
        user.ushow = post.get('ushou', None)
        user.uaddress = post.get('uaddress', None)
        user.uyoubian = post.get('uyoubian', None)
        user.uphone = post.get('uphone', None)
        user.save()
        # print(user)
    context = {
        'title': '用户中心',
        'user': user,
        'page_name': 1
    }
    return render(request, 'df_user/user_center_site.html', context)


@user_decorator.login
def order(request):
    context = {
        'title': '用户中心',
        'page_name': 1
    }
    return render(request, 'df_user/user_center_order.html', context)
