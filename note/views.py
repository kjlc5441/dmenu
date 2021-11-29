from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Note, NoteB, NoteC,Store


# Create your views here.

# 登入校驗 裝飾器寫法


def check_login(fn):
    def wrap(request, *args, **kwargs):
        # 檢查session內的字典 是否登入中
        if 'username' not in request.session or 'uid' not in request.session:
            # 如果session沒有 再檢查cookies內設定的兩個參數
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                # 回寫session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap


@check_login  # 登入校驗
def list_note(request, list_id):
    print("note_id=",list_id)
    # return HttpResponse("list_id views is ok")
    if list_id==1:
        all_item = Note.objects.filter(is_active=True)
        return render(request, "note/list_note.html", locals())
    elif list_id==2:
        all_item = NoteB.objects.filter(is_active=True)
        return render(request, "note/list_noteB.html", locals())
    elif list_id==3:
        all_item = NoteC.objects.filter(is_active=True)
        return render(request, "note/list_noteC.html", locals())
    elif list_id==4:
        # 修改店名 固定為第一筆
        all_item = Store.objects.get(id=1)
        return render(request, "note/list_store.html", locals())


@check_login  # 登入校驗
def add_note(request):
    if request.method == 'GET':
        # locals()傳遞get_path資料到html
        return render(request, 'note/add_note.html',locals())

    elif request.method == 'POST':
        # 處理數據
        uid = request.session['uid']
        title = request.POST['title']
        plu = request.POST['plu']
        name = request.POST['name']
        content = request.POST["content"]
        price = request.POST["price"]
        saleout = request.POST["saleout"]

        # 判斷空值 2正確區位範圍 3資料重複
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
        
        if 'A' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: A1~A8</h1>")
    
        try:
            title_double = Note.objects.filter(is_active=True,title=title)
            print('title_double:',title_double)
        except Exception as e:
            title_double = None
        if title_double:
            return HttpResponse("<h1>Error-Code: 設定區位-已被使用</h1>")

        #保存
        Note.objects.create(title=title, plu=plu,name=name,content=content, price=price,saleout=saleout,user_id=uid)

        # return HttpResponse('添加筆記成功')
        # 執行確認頁面 同時處理頁面跳轉 到前一頁
        return HttpResponseRedirect("1")


@check_login  # 登入校驗
def add_noteB(request):
    if request.method == 'GET':
        # locals()傳遞get_path資料到html
        return render(request, 'note/add_noteB.html',locals())

    elif request.method == 'POST':
        # 處理數據
        uid = request.session['uid']
        title = request.POST['title']
        plu = request.POST['plu']
        name = request.POST['name']
        content = request.POST["content"]
        price = request.POST["price"]
        saleout = request.POST["saleout"]

         # 判斷空值 2正確區位範圍 3資料重複
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
        
        if 'B' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: B1~</h1>")
    
        try:
            title_double = NoteB.objects.filter(is_active=True,title=title)
            print('title_double:',title_double)
        except Exception as e:
            title_double = None
        if title_double:
            return HttpResponse("<h1>Error-Code: 設定區位-已被使用</h1>")
        
        #保存
        NoteB.objects.create(title=title, plu=plu,name=name, content=content, price=price,saleout=saleout,user_id=uid)

        # return HttpResponse('添加筆記成功')
        # 執行確認頁面 同時處理頁面跳轉 到前一頁
        return HttpResponseRedirect("2")


@check_login  # 登入校驗
def add_noteC(request):
    if request.method == 'GET':
        # locals()傳遞get_path資料到html
        return render(request, 'note/add_noteC.html',locals())

    elif request.method == 'POST':
        # 處理數據
        uid = request.session['uid']
        title = request.POST['title']
        plu = request.POST['plu']
        name = request.POST['name']
        content = request.POST["content"]
        price = request.POST["price"]
        saleout = request.POST["saleout"]

        # 判斷空值 2正確區位範圍 3資料重複
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
        
        if 'C' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: C1~</h1>")
    
        try:
            title_double = NoteC.objects.filter(is_active=True,title=title)
            print('title_double:',title_double)
        except Exception as e:
            title_double = None
        if title_double:
            return HttpResponse("<h1>Error-Code: 設定區位-已被使用</h1>")


        #保存
        NoteC.objects.create(title=title, plu=plu,name=name, content=content, price=price,saleout=saleout,user_id=uid)

        # return HttpResponse('添加筆記成功')
        # 執行確認頁面 同時處理頁面跳轉 到前一頁
        return HttpResponseRedirect("3")


@check_login  # 登入校驗
def mod_note(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000:/note/mod_note/1
    # 修改models資料步驟 1.查
    try:
        item = Note.objects.get(id=note_id, is_active=True)
        # print("note_id=", note_id)
        # print("對象資料：", item)
    except Exception as e:
        print("--update note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    if request.method == "GET":
        print('mod_note:', item)
        # locals()傳遞item資料到html
        # return HttpResponse("test OK")
        return render(request, "note/mod_note.html", locals())
        
    elif request.method == "POST":
        title = request.POST["title"]
        plu = request.POST["plu"]
        name = request.POST["name"]
        content = request.POST["content"]
        price=request.POST["price"]
        saleout=request.POST["saleout"]

        # 判斷1空值 2正確區位範圍
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
     
        if 'A' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: A1~A8</h1>")

        # 2.改
        item.title = title
        item.plu = plu
        item.name = name
        item.content = content
        item.price = price
        item.saleout = saleout
        
        # 3.保存
        item.save()
        print("save_item:",item)

        # 執行確認頁面 同時處理頁面跳轉 設定於form-action內
        # return render(request, "note/mod_note.html", locals())
        return HttpResponseRedirect("/note/1")


@check_login  # 登入校驗
def mod_noteB(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000:/note/mod_noteB/1
    # 修改models資料步驟 1.查
    try:
        item = NoteB.objects.get(id=note_id, is_active=True)
        # print("note_id=", note_id)
        # print("對象資料：", item)
    except Exception as e:
        print("--update note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    if request.method == "GET":
        print('mod_noteB:', item)
        # locals()傳遞item資料到html
        # return HttpResponse("test OK")
        return render(request, "note/mod_noteB.html", locals())

    elif request.method == "POST":
        title = request.POST["title"]
        plu = request.POST["plu"]
        name = request.POST["name"]
        content = request.POST["content"]
        price=request.POST["price"]
        saleout=request.POST["saleout"]

        # 判斷1空值 2正確區位範圍
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
     
        if 'B' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: B1~</h1>")

        # 2.改
        item.title = title
        item.plu = plu
        item.name = name
        item.content = content
        item.price = price
        item.saleout = saleout
        # 3.保存
        item.save()
        print("save_item:",item)

        # 執行確認頁面 同時處理頁面跳轉 設定於form-action內
        # return render(request, "note/mod_note.html", locals())
        return HttpResponseRedirect("/note/2")


@check_login  # 登入校驗
def mod_noteC(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000:/note/mod_noteC/1
    # 修改models資料步驟 1.查
    try:
        item = NoteC.objects.get(id=note_id, is_active=True)
        # print("note_id=", note_id)
        # print("對象資料：", item)
    except Exception as e:
        print("--update note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    if request.method == "GET":
        print('mod_noteC:', item)
        # locals()傳遞item資料到html
        # return HttpResponse("test OK")
        return render(request, "note/mod_noteC.html", locals())
        
    elif request.method == "POST":
        title = request.POST["title"]
        plu = request.POST["plu"]
        name = request.POST["name"]
        content = request.POST["content"]
        price=request.POST["price"]
        saleout=request.POST["saleout"]

         # 判斷1空值 2正確區位範圍
        if not title:
            return HttpResponse("<h1>Error-Code: 沒有設定-顯示區位</h1>")
     
        if 'C' not in title:
            return HttpResponse("<h1>Error-Code: 正確區位範圍: C1~</h1>")
       
        # 2.改
        item.title = title
        item.plu = plu
        item.name = name
        item.content = content
        item.price = price
        item.saleout = saleout
        # 3.保存
        item.save()
        print("save_item:",item)

        # 執行確認頁面 同時處理頁面跳轉 設定於form-action內
        # return render(request, "note/mod_note.html", locals())
        return HttpResponseRedirect("/note/3")


@check_login  # 登入校驗
def back_note(request, note_id):
    # return HttpResponse("mod_note views is ok")
    print("get note_id=", note_id)
    # 前端傳來路徑note/back_note/1
    # 修改models資料步驟 1.查
    try:
        note = Note.objects.get(id=note_id, is_active=True)
        print("對象資料：", note)
    except Exception as e:
        print("--update note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    if request.method == "GET":
        # locals()為某一個id編號的對象,是一組字典,傳到模板取出各字段
        get_path = request.META.get('HTTP_REFERER')
        print('get_path:', get_path)
        return render(request, "note/back_note.html", locals())

    elif request.method == "POST":
        # 主要返回路徑 設定於form_action內
        return HttpResponseRedirect("")


@check_login  # 登入校驗
def del_note(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000/note/del_note/1
    # get請求後 取得最後一個/後的數字 傳回函數成為note_id參數值
    print("get note_id=", note_id)

    if not note_id:
        return HttpResponse("請求異常")
    try:
        note = Note.objects.get(id=note_id, is_active=True)
        print("對象資料=", note)
    except Exception as e:
        print("--delete note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    # 將其is_active 改成False
    note.is_active = False
    note.save()
    # 執行刪除後302挑轉 無法確認返回頁碼 先設定第一頁
    return HttpResponseRedirect('/note/1')


@check_login  # 登入校驗
def del_noteB(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000/note/del_note/1
    # get請求後 取得最後一個/後的數字 傳回函數成為note_id參數值
    print("get noteB_id=", note_id)

    if not note_id:
        return HttpResponse("請求異常")
    try:
        note = NoteB.objects.get(id=note_id, is_active=True)
        print("B對象資料=", note)
    except Exception as e:
        print("--delete note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    # 將其is_active 改成False
    note.is_active = False
    note.save()
    # 執行刪除後302挑轉 無法確認返回頁碼 先設定第一頁
    return HttpResponseRedirect('/note/2')   


@check_login  # 登入校驗
def del_noteC(request, note_id):
    # urls有<int轉換器>127.0.0.1:8000/note/del_note/1
    # get請求後 取得最後一個/後的數字 傳回函數成為note_id參數值
    print("get noteC_id=", note_id)

    if not note_id:
        return HttpResponse("請求異常")
    try:
        note = NoteC.objects.get(id=note_id, is_active=True)
        print("C對象資料=", note)
    except Exception as e:
        print("--delete note error id %s" % (e))
        return HttpResponse("--The note is not existed")

    # 將其is_active 改成False
    note.is_active = False
    note.save()
    # 執行刪除後302挑轉 無法確認返回頁碼 先設定第一頁
    return HttpResponseRedirect('/note/3')   


@check_login  # 登入校驗
def add_store(request):
    if request.method == 'GET':
        # return HttpResponse("store_id views is ok")
        return render(request, 'note/add_store.html',locals())

    elif request.method == 'POST':
        # 處理數據
        uid = request.session['uid']
        store_name = request.POST['store_name']
        store_tel = request.POST['store_tel']

        # 判斷空值 2正確區位範圍 3資料重複
        if not store_name:
            return HttpResponse("<h1>Error-Code: 沒有設定-店名</h1>")
        
        if not store_tel:
            return HttpResponse("<h1>Error-Code: 沒有設定-電話</h1>")

        #保存
        Store.objects.create(store_name=store_name, store_tel=store_tel)

        # 執行確認頁面 同時處理頁面跳轉 到前一頁
        return HttpResponseRedirect("4")


@check_login  # 登入校驗
def mod_store(request):
    # 修改models資料步驟 1.查
    try:
        item = Store.objects.get(id=1)
     
    except Exception as e:
        print("--update store error id %s" % (e))
        return HttpResponse("--The store is not existed")

    if request.method == "GET":
        # return HttpResponse("test OK")
        return render(request, "note/mod_store.html", locals())
        
    elif request.method == "POST":
        store_name = request.POST["store_name"]
        store_tel = request.POST["store_tel"]
      
        # 判斷1空值 2正確區位範圍
        if not store_name:
            return HttpResponse("<h1>Error-Code: 沒有設定-店名</h1>")
        
        if not store_tel:
            return HttpResponse("<h1>Error-Code: 沒有設定-電話</h1>")
        # 2.改
        item.store_name = store_name
        item.store_tel = store_tel
     
        # 3.保存
        item.save()
        print("save_item:",item)

        # 執行確認頁面 同時處理頁面跳轉 設定於form-action內
        return HttpResponseRedirect("4")