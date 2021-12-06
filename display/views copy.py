from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from note.models import Note,NoteB,NoteC,Store
import json
from decimal import Decimal
from datetime import datetime


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


def tv1(request):
    A1 = Note.objects.get(title='A1', is_active=True)
    A2 = Note.objects.get(title='A2', is_active=True)
    A3 = Note.objects.get(title='A3', is_active=True)
    A4 = Note.objects.get(title='A4', is_active=True)
    A5 = Note.objects.get(title='A5', is_active=True)
    A6 = Note.objects.get(title='A6', is_active=True)
    # return HttpResponse("tv1_html is ok")

    all_item = Note.objects.filter(is_active=True)
    note_title=[]
    note_saleout=[]
    note_dic =[]
    for i in all_item:
        note_title.append(i.title)
        note_saleout.append(i.saleout)
        note_dic = dict(map(lambda x,y:[x,y],note_title,note_saleout))
    print(note_dic )
    JsonTitle=json.dumps(note_title)    
    JsonSaleout=json.dumps(note_saleout)
    JsonNote_dic=json.dumps(note_dic)
    return render(request, "display/tv1.html", locals())


def tv2(request):
    A7 = Note.objects.get(title='A7', is_active=True)
    A8 = Note.objects.get(title='A8', is_active=True)
    B1= NoteB.objects.get(title='B1', is_active=True)
    B2= NoteB.objects.get(title='B2', is_active=True)
    store=Store.objects.get(id=1)

    all_item = Note.objects.filter(is_active=True)
    note_title=[]
    note_saleout=[]
    note_dic =[]
    for i in all_item:
        note_title.append(i.title)
        note_saleout.append(i.saleout)
        note_dic = dict(map(lambda x,y:[x,y],note_title,note_saleout))
    JsonTitle=json.dumps(note_title)    
    JsonSaleout=json.dumps(note_saleout)
    JsonNote_dic=json.dumps(note_dic)
    # return render(request, "display/tv2.html", locals())
    return render(request, "display/tv2.html", locals())


def tv2_0(request):
    A7 = Note.objects.get(title='A7', is_active=True)
    A8 = Note.objects.get(title='A8', is_active=True)
    # return HttpResponse("tv2_0_html is ok")

    all_item = Note.objects.filter(is_active=True)
    note_title=[]
    note_saleout=[]
    note_dic =[]
    for i in all_item:
        note_title.append(i.title)
        note_saleout.append(i.saleout)
        note_dic = dict(map(lambda x,y:[x,y],note_title,note_saleout))
    print(note_dic )
    JsonTitle=json.dumps(note_title)    
    JsonSaleout=json.dumps(note_saleout)
    JsonNote_dic=json.dumps(note_dic)
    return render(request, "display/tv2_A7A8.html", locals())


def tv2_1(request):
    B1= NoteB.objects.get(title='B1', is_active=True)
    B2= NoteB.objects.get(title='B2', is_active=True)
    all_item = NoteB.objects.filter(is_active=True)
    noteB_content=[]
    noteB_price=[]
    noteB_title=[]
    noteB_saleout=[]
    note_dic =[]
    for i in all_item:
        noteB_title.append(i.title)
        noteB_content.append(i.content)
        noteB_price.append(i.price)
        noteB_saleout.append(i.saleout)
        noteB_dic=dict(map(lambda x,y:[x,y],noteB_title,noteB_saleout)) 
    print("B:",noteB_title,noteB_content,noteB_price,noteB_dic)
    JsonContent=json.dumps(noteB_content)
    JsonPrice = json.dumps(noteB_price, cls=DecimalEncoder)
    JsonSaleout=json.dumps(noteB_saleout)
    JsonNoteB_dic=json.dumps(noteB_dic)
    # return HttpResponse("tv2_html is ok")
    return render(request, "display/tv2_2circle.html", locals())


def tv2_2(request):
    all_item = NoteC.objects.filter(is_active=True)
    noteC_content=[]
    for i in all_item:
        noteC_content.append(i.content)
    print ("noteC_content:",noteC_content)
    JsonContent=json.dumps(noteC_content)

    noteC_price=[]
    for j in all_item:
        noteC_price.append(j.price)
   
    # JsonPrice=json.dumps(noteC_price)
    JsonPrice = json.dumps(noteC_price, cls=DecimalEncoder)
    print ("JsonPrice:",JsonPrice)
    # return HttpResponse("tv2_2html is ok")
    return render(request, "display/tv2_8circle.html", locals())


class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)



