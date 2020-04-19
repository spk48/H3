from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

import wehouse.views as views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^index', views.index, name='index'),
                  url(r'^categories', views.categories, name='categories'),
                  url(r'^login',views.login,name='login'),
                  url(r'^logout',views.logout,name='logout'),
                  url(r'^register',views.register,name = 'register'),
                  url(r'^contact',views.contact,name = 'contact'),
                  url(r'^profile',views.profile,name = 'profile'),
                  url(r'^change_profile',views.change_profile,name = 'change_profile'),
                  url('cart.html',views.cart,name = 'cart'),
                  url('owned.html',views.owned,name = 'owned'),
                  url('owned_house.html',views.owned_house,name = 'owned_house'),
                  url('regist_house.html',views.regist_house,name = 'regist_house'),
                  url(r'^house/detail$',views.house_details,name = 'house_details'),
                  url(r'^get_house$',views.get_house,name = 'get_house'),
                  url(r'^cart_buy.html',views.cart_buy,name = 'cart_buy'),
                  url(r'^cart_get.html',views.cart_get,name = 'cart_get'),
                  url(r'^yes$',views.yes,name = 'yes'),
                  url(r'^no$',views.no,name = 'no'),
                  url(r'^test',views.test,name = 'test'),
              ]
