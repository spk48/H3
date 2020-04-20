from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

import uuid, os


def custom_path(instance, filename):
    ext = filename.split('.')[ -1 ]
    filename = '{}.{}'.format(uuid.uuid4().hex[ :10 ], ext)
    return filename


class Customers(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')  # 和Django的用户一对一对应
    UID = models.CharField(max_length = 45, unique = True, verbose_name = 'UID')
    Uname = models.CharField(max_length = 45, null = False, verbose_name = 'Uname')
    Unation = models.CharField(max_length = 45, null = False, verbose_name = 'Unation')  # 国籍
    Ugender = models.CharField(max_length = 45, verbose_name = 'Ugender')
    Uage = models.CharField(max_length = 45, verbose_name = 'Uage')
    Ulis_kind = models.CharField(max_length = 45, null = False, verbose_name = 'Ulis_kind')  # 证件类型
    Ulis_num = models.CharField(max_length = 45, null = False, verbose_name = 'Ulis_num')  # 号码
    Ucontent = models.CharField(max_length = 45, null = False, verbose_name = 'Ucontent')  # 联系方式
    staff=models.IntegerField(default = 0)

    def __str__(self):
        return self.Uname + '(' + self.UID + ')'


class House(models.Model):
    HID = models.CharField(max_length = 45, primary_key = True, verbose_name = 'HID')
    Howner = models.ForeignKey('Customers', on_delete = models.CASCADE)  # 房子和用户，多对一。先用户后产生房子。
    # Howner = models.CharField(max_length = 45, primary_key = True, verbose_name = 'Howner')
    Hname = models.CharField(max_length = 45, null = False, verbose_name = 'Hname')
    Hprice = models.CharField(max_length = 45, null = False, verbose_name = 'Hprice')
    Haddress = models.CharField(max_length = 100, null = False, verbose_name = 'Haddress')
    Hcontect = models.CharField(max_length = 45, verbose_name = 'Hcontect')
    Hdecoration = models.CharField(max_length = 45, verbose_name = 'Hdecoration')
    Hkind = models.CharField(max_length = 45, null = False, verbose_name = 'Hkind')
    Hnature = models.CharField(max_length = 45, verbose_name = 'Hnature')
    Harea = models.CharField(max_length = 45, null = False, verbose_name = 'Harea')
    Hcover_area = models.CharField(max_length = 45, null = False, verbose_name = 'Hcover_area')
    Hgift = models.CharField(max_length = 45, verbose_name = 'Hgift')
    PID = models.CharField(max_length = 15, null = False, verbose_name = 'PID')
    CID = models.CharField(max_length = 15, null = False, verbose_name = 'CID')
    VID = models.CharField(max_length = 15, null = False, verbose_name = 'VID')
    Hpic = models.ImageField(blank = True, upload_to = custom_path, verbose_name = 'Hpic')  # 房子图像
    HOT = models.IntegerField(default = 0)

    def __str__(self):
        return self.Howner + ' ' + self.Hname + '(' + self.HID + ')' + self.PID + ' ' + self.CID + ' ' + self.VID


class Business(models.Model):
    # UID = models.CharField(max_length = 45, primary_key = True, verbose_name = 'UID')
    # HID = models.CharField(max_length = 45, primary_key = True, verbose_name = 'HID')
    BID = models.CharField(max_length = 45, primary_key = True, blank = True,verbose_name = 'BID')
    Bstatus = models.CharField(max_length = 45, verbose_name = 'Bstatus')
    Btime = models.DateTimeField(auto_now_add = True, editable = False, verbose_name = 'Btime')  # 订单创建时间
    Btime_after = models.CharField(verbose_name = 'Btime_after',max_length=45)  # 交易时间
    Bprice = models.CharField(max_length = 45, verbose_name = 'Bprice')
    Bcost = models.CharField(max_length = 45, verbose_name = 'Bcost')
    UID = models.ForeignKey('Customers', on_delete = models.CASCADE)
    HID = models.ForeignKey('House', on_delete = models.CASCADE)

    def __str__(self):
        return self.UID + ' ' + self.HID
