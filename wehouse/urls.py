from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

import wehouse.views as views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^login',views.login,name='login'),
                  url(r'^logout',views.logout,name='logout'),
                  url(r'^register',views.register,name = 'register'),
                  url(r'^contact',views.contact,name = 'contact'),
                  url(r'^profile',views.profile,name = 'profile'),
                  url(r'^change_profile',views.change_profile,name = 'change_profile'),
                  url(r'^test',views.test,name = 'test'),
              ]
