from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import hashlib

# Create your views here.\

def reg_view(request):
    # 註冊
    # GET返回頁面
    if request.method == 'GET':
        return render(request, 'user/register.html')
    # POST提交數據
    elif request.method == 'POST':
        # return HttpResponse('POST響應')
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

    # 1 檢查兩個密碼是否一致
    if password_1 != password_2:
        return HttpResponse("<h1>兩次密碼不一樣</h1>")

    # 引入哈希算法
    m = hashlib.md5()
    m.update(password_1.encode())
    password_m = m.hexdigest()

    # 2 當前用戶是否可用
    old_users = User.objects.filter(username=username)
    if old_users:
        return HttpResponse('<h1>名稱已註冊過</h1>')

    # 3 多台主機服務 可能沒有過濾到 於存入資料庫時 再把關一次
    try:
        user = User.objects.create(username=username, password=password_m)
    except Exception as e:
        print('--建檔異常--%s'%(e))
        return HttpResponse('<h1>用戶名已註冊</h1>')

    # 已開帳號 可免登入一天
    request.session['username']=username
    request.session['uid']=user.id
    # 修改session預設30天為1天

    # return HttpResponse('註冊成功')
    return HttpResponseRedirect('/index')


def login_view(request):
    # 註冊
    # GET返回頁面
    if request.method == 'GET':
        # 檢查用戶是否有一天內登入的session紀錄(紀錄是一組字典）
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登入_s')
            return HttpResponseRedirect('/index')
        # # 檢查用戶是否有三天內登入的cookie紀錄(紀錄是預定的兩個參數)
        c_username = request.COOKIES.get('username')
        c_id = request.COOKIES.get('uid')
        if c_username and c_id:
            # 回寫session一份
            request.session['username'] = c_username
            request.session['uid'] = c_id
            # return HttpResponse('已登入_c')
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')

    # POST提交數據
    elif request.method == 'POST':
        # return HttpResponse('登入成功')
        username = request.POST['username']
        password = request.POST['password']

        try:
            user =User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('<h1>登入資訊有誤！</h1>')

        # 檢查密碼
        # 引入哈希算法
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('<h1>登入資訊有誤！</h1>')

        # 目標 開帳號當日 一天內免登入 採用session方案
        request.session['username'] = username
        request.session['uid'] = user.id
        # 修改session預設14天為1天

        # resp = HttpResponse('登入成功')
        resp = HttpResponseRedirect('/index')
        # 判斷客戶點選'記住我'三天內免登入 採用cookie方案
        # 點選'記住我'POST回來一組字典 包含name="remember"
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)
        return resp


def logout_view(request):
    #刪除session 字典內的值
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect('/index')
    # 刪除cookies 設定的兩個值
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp




