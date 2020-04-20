from typing import Dict, List, Any, Union

from django.contrib.auth.models import User
from django.core import paginator
from django.shortcuts import render

# Create your views here.

import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from wehouse.models import House,Business,Customers
from django import forms
import hashlib
import time
from django.db.models import Q
import random


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label=u'用户名：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        })
    )
    password = forms.CharField(
        label=u'密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'id': 'id_password',
        }),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label=u'用户名',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        }),
    )
    nickname = forms.CharField(
        label = u'昵称',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'nickname',
            'id': 'id_nickname',
        }),
    )
    password = forms.CharField(
        label=u'密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'id': 'id_password',
        }),
    )
    re_password = forms.CharField(
        label=u'重复密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 're_password',
            'id': 'id_re_password',
        }),
    )
    phone_number = forms.CharField(
        label = u'手机号码：',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'phone_number',
            'id': 'id_phone_number',
        }),
    )
    Ulis_kind = forms.CharField(
        label = u'证件类型：',
        widget = forms.Select(choices = [
            ('身份证', '身份证'),
            ('中华人民共和国护照', '中华人民共和国护照'),
            ('机动车驾驶证', '机动车驾驶证'),
        ]),
    )
    Ulis_num = forms.CharField(
        max_length = 20,
        label = u'证件号码：',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'Ulis_num',
            'id': 'id_Ulis_num',
        })
    )


class ProfileForm(forms.Form):
    username = forms.CharField(
        label = u'昵称',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        }),
    )
    age = forms.CharField(
        label = u'年龄',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'age',
            'id': 'id_age',
        }),
    )
    gender = forms.CharField(
        label = u'性别',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'gender',
            'id': 'id_gender',
        }),
    )
    nation = forms.CharField(
        label = u'国籍',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'nation',
            'id': 'id_nation',
        }),
    )
    phone_number = forms.CharField(
        label = u'手机号码：',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'phone_number',
            'id': 'id_phone_number',
        }),
    )
    Ulis_kind = forms.CharField(
        label = u'证件类型：',
        widget = forms.Select(choices = [
            ('身份证', '身份证'),
            ('中华人民共和国护照', '中华人民共和国护照'),
            ('机动车驾驶证', '机动车驾驶证'),
        ]),
    )
    Ulis_num = forms.CharField(
        max_length = 20,
        label = u'证件号码：',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'Ulis_num',
            'id': 'id_Ulis_num',
        })
    )


class HouseDetail(forms.Form):
    PID = forms.CharField(
        label = u'省',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'PID',
            'id': 'id_PID',
        }),
    )
    CID = forms.CharField(
        label = u'市',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'CID',
            'id': 'id_CID',
        }),
    )
    VID = forms.CharField(
        label = u'区',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'VID',
            'id': 'id_VID',
        }),
    )

    name = forms.CharField(
        label = u'房屋名',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'name',
            'id': 'id_name',
        }),
    )
    address =forms.CharField(
        label = u'完整地址',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'address',
            'id': 'id_address',
        }),
    )
    price = forms.CharField(
        label = u'房屋价格',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'price',
            'id': 'id_price',
        }),
    )
    content=forms.CharField(
        label = u'房屋描述',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'content',
            'id': 'id_content',
        }),
    )
    decoration = forms.CharField(
        label = u'装修',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'decoration',
            'id': 'id_decoration',
        }),
    )
    kind = forms.CharField(
        label = u'房屋类型',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'kind',
            'id': 'id_kind',
        }),
    )
    nature = forms.CharField(
        label = u'房屋性质',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'nature',
            'id': 'id_nature',
        }),
    )
    area = forms.CharField(
        label = u'房屋建筑面积',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'nature',
            'id': 'id_nature',
        }),
    )
    cover_area = forms.CharField(
        label = u'房屋占地面积',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'cover_area',
            'id': 'id_cover_area',
        }),
    )
    gift = forms.CharField(
        max_length = 20,
        label = u'房屋附带服务：',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'name': 'gift',
            'id': 'id_gift',
        })
    )
    photo = forms.FileField(
        label = u'房屋照片：',
        widget = forms.FileInput(attrs = {
            'class': 'form-control',
            'name': 'photo',
            'id': 'id_photo',
        }),
        required = False,
    )


def index(request):
    return render(request, 'H3/index.html')


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    state = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse(u'Your account is disabled.')
        else:
            state = 'not_exist_or_password_error'

    context = {
        'loginForm': LoginForm(),
        'state': state,
    }

    return render(request, 'H3/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    registerform = RegisterForm()

    state = None
    if request.method == 'POST':
        registerform = RegisterForm(request.POST, request.FILES)
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('re_password', '')
        ulis_kind=request.POST.get('Ulis_kind','')
        ulis_num=request.POST.get('Ulis_num','')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            name = request.POST.get('name', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create(username=username)
                new_user.set_password(password)
                new_user.save()
                new_customers = Customers.objects.create(user = new_user, UID=new_user.id, Uname = username,
                                                      Ulis_kind = ulis_kind,Ulis_num = ulis_num)
                new_customers.save()
                state = 'success'

                auth.login(request, new_user)

                context = {
                    'state': state,
                    'registerForm': registerform,
                }
                return render(request, 'H3/register.html', context)

    context = {
        'state': state,
        'registerForm': registerform,
    }

    return render(request, 'H3/register.html', context)


def test(request):
    return render(request, 'H3/test.html')


def contact(request):
    return render(request, 'H3/contact.html')


def change_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        customer=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    #倘若是POST、则更改信息
    if request.method=='POST':
        customer.Uage=request.POST.get('age','')
        customer.Uname=request.POST.get('username','')
        customer.Ugender=request.POST.get('gender','')
        customer.Unation=request.POST.get('nation','')
        customer.Ulis_kind=request.POST.get('Ulis_kind','')
        customer.Ulis_num=request.POST.get('Ulis_num','')
        customer.Ucontent=request.POST.get('phone_number','')
        customer.save()
        context = {
            'state': request.GET.get('state', None),
            'customer': customer,
        }
        return render(request,'H3/profile.html',context)

    profileform = ProfileForm(request.POST or None,
                              initial = {
                                  'username':customer.Uname,
                                  'age':customer.Uage,
                                  'gender':customer.Ugender,
                                  'nation':customer.Unation,
                                  'Ulis_kind': customer.Ulis_kind,
                                  'Ulis_num':customer.Ulis_num,
                                  'phone_number':customer.Ucontent,
                              })
    context={
        'state':request.GET.get('state',None),
        'customer':customer,
        'ProfileForm':profileform,
    }
    return render(request,'H3/change_profile.html',context)


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')

    id = request.user.id;
    try:
        customer = Customers.objects.get(user_id = id)
        user=User.objects.get(customers__UID = id)
    except Customers.DoesNotExist:
        return HttpResponse('/ERROR.html')

    context = {
        'state': request.GET.get('state', None),
        'customer': customer,
        'user':user,
    }
    return render(request,'H3/profile.html',context)


def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id = request.user.id
    try:
        customer = Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    context={
        "customer":customer,
    }
    return render(request,'H3/cart.html',context)


def owned(request):
    return render(request,'H3/owned.html')


def owned_house(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        customer=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    houses=House.objects.filter(Howner_id = customer.id)
    context={
        'state':request.GET.get('state',None),
        'customer':customer,
        'houses':houses,
    }
    return render(request,'H3/owned_house.html',context)


def regist_house(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id = request.user.id
    try:
        customer = Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')

    house_details = HouseDetail(request.POST or None)

    state = None

    if request.method == 'POST':

        house_details = HouseDetail(request.POST, request.FILES)
        gift = request.POST.get('gift','')
        name=request.POST.get('name','')
        price=request.POST.get('price','')

        cover_area = request.POST.get('cover_area', '')
        area = request.POST.get('area', '')
        nature = request.POST.get('nature', '')
        kind = request.POST.get('kind', '')
        decoration = request.POST.get('decoration', '')
        content = request.POST.get('content', '')
        address = request.POST.get('address', '')
        VID = request.POST.get('VID', '')
        CID = request.POST.get('CID', '')
        PID = request.POST.get('PID', '')
        photo=request.FILES.get('photo','')
        __HID=hash(house_details.__str__()+address+PID+CID+VID+content)
        if House.objects.filter(HID=__HID):
                state = 'exist'
        else:
            new_house = House.objects.create(HID=__HID,
                                             PID=PID,
                                             CID=CID,
                                             VID=VID,
                                             Howner =customer,
                                             Hname = name,
                                             Hprice = price,
                                             Haddress = address,
                                             Hcontect = content,
                                             Hcover_area = cover_area,
                                             Harea = area,
                                             Hnature = nature,
                                             Hkind = kind,
                                             Hdecoration = decoration,
                                             Hgift = gift,
                                             Hpic = photo)
            new_house.save()
            state = 'success'
            context = {
                'state': state,
                'registerForm': house_details,
            }
            return render(request, 'H3/regist_house.html', context)

    context = {
        'state': state,
        'registerForm': house_details,
    }
    return render(request,'H3/regist_house.html',context)

# request传入HID
def house_details(request):
    #获取当前查看房子id,HID
    house_id=request.GET.get('HID',None)
    if not house_id:
            return render(request,'H3/ERROR.html')
    try:
        house_detail=House.objects.get(HID = house_id)
    except House.DoesNotExist:
        return render(request,'H3/ERROR.html')
    try:
        owner = Customers.objects.get(id = house_detail.Howner_id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    #获取当前用户信息
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        customer=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    house_detail.HOT+=1
    house_detail.save()
    context={
        'state':request.GET.get('state',None),
        'house_detail':house_detail,
        'owner':owner,
        'customer':customer,
    }
    return render(request,'H3/house_details.html',context)

# request传入HID
def get_house(request):
    state=None
    #me
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id = request.user.id
    try:
        me = Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')

    #购买房子的信息
    house_id=request.GET.get('HID',None)
    if not house_id:
            return render(request,'H3/ERROR.html')
    try:
        house_detail=House.objects.get(HID = house_id)
    except House.DoesNotExist:
        return render(request,'H3/ERROR.html')
    #获取房主
    try:
        owner = Customers.objects.get(id = house_detail.Howner_id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    #0 有效订单，1 已经成交，2 订单废弃
    new_business=Business.objects.create(Bstatus = 0,
                                         HID=house_detail,
                                         UID = me,
                                         Bprice = house_detail.Hprice,
                                         Bcost = house_detail.Hprice,
                                         BID=hash(time.time()))
    new_business.save()
    state="success"
    context={
        'state':state,
    }
    return render(request,'H3/get_house.html',context)

def cart_buy(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        me=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')

    bs=Business.objects.filter(UID_id = me.id)
    context={
        'state':request.GET.get('state',None),
        'me':me,
        'bs':bs,
    }
    return render(request,'H3/cart_buy.html',context)


def cart_get(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        me=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    bs=Business.objects.all()
    context={
        'state':request.GET.get('state',None),
        'me':me,
        'bs':bs,
    }
    return render(request,'H3/cart_get.html',context)


def yes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        me=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    try:
        bid=request.GET.get('BID','')
        new_bs=Business.objects.get(BID=bid)
    except Exception:
        return render(request,'H3/ERROR.html')

    house=new_bs.HID
    new_owner=new_bs.UID
    house.Howner=new_owner
    new_bs.Bstatus=1
    other_bs=Business.objects.filter(HID = house)
    for i in other_bs:
        i.Bstatus=2
        i.save()
    house.save()
    new_bs.save()
    try:
        bs=Business.objects.all()
    except Exception:
        return render(request,'H3/ERROR.html')
    context = {
        'state': request.GET.get('state', None),
        'me': me,
        'bs': bs,
    }
    return render(request,'H3/cart_get.html',context)


def no(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id = request.user.id
    try:
        me = Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request, 'H3/ERROR.html')
    try:
        bid = request.GET.get('BID', '')
        new_bs = Business.objects.get(BID = bid)
    except Exception:
        return render(request, 'H3/ERROR.html')

    new_bs.Bstatus = 2
    new_bs.save()
    try:
        bs = Business.objects.all()
    except Exception:
        return render(request, 'H3/ERROR.html')
    context = {
        'state': request.GET.get('state', None),
        'me': me,
        'bs': bs,
    }
    return render(request, 'H3/cart_get.html', context)


def categories(request):
    id=request.user.id
    houses=House.objects.all()
    context={
        'state':request.GET.get('state',None),
        'houses':houses,
    }
    return render(request,'H3/categories.html',context)


def search(request):
    kw=request.GET.get('keyword','')
    kwlist=list(map(str,kw.strip().split()))
    filters=Q()
    for n in kwlist:
        filters = Q(Hname=n)|Q(PID=n)|Q(CID=n)|Q(VID=n)|filters
    result=House.objects.filter(filters)
    context={
        'houses':result,
    }
    return render(request,'H3/search.html',context)


def hot(request):
    list=House.objects.all().order_by('-HOT')[:10]
    context={
        'houses':list
    }
    return render(request,'H3/categories.html',context)


def today_is_a_nice_day(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        customer=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return render(request,'H3/ERROR.html')
    list=House.objects.all()
    house=list[random.randint(0,list.count()-1)]
    try:
        owner = Customers.objects.get(id = house.Howner_id)
    except Customers.DoesNotExist:
        return render(request, 'H3/ERROR.html')
    context = {
        'house_detail': house,
        'owner':owner,
        'customer':customer,
    }
    return render(request, 'H3/house_details.html', context)