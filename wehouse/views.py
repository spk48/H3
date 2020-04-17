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
        return HttpResponse('H3/ERROR.html')
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
    return render(request,'H3/cart.html')


def owned(request):
    return render(request,'H3/owned.html')


def owned_house(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login.html')
    id=request.user.id
    try:
        customer=Customers.objects.get(user_id = id)
    except Customers.DoesNotExist:
        return HttpResponse('H3/ERROR.html')
    houses=House.objects.filter(Howner_id = customer.user_id)
    context={
        'state':request.GET.get('state',None),
        'customer':customer,
        'houses':houses,
    }
    return render(request,'H3/owned_house.html',context)


def regist_house(request):
    return render(request,'H3/regist_house.html')


def house_details(request):
    return render(request,'H3/house_details.html')