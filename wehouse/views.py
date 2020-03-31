from django.core import paginator
from django.shortcuts import render

# Create your views here.

import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wehouse.models import House,Business,Customers


def index(requset):
    customers=Customers.objects.all()
    context={
        'customers' : customers,
    }
    return render(requset, 'H3/index.html', context)

