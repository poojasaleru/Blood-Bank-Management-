"""BBM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('login',views.log,name="login"),
    path('miniproject',views.login,name="login"),
    path('si',views.si,name="si"),
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('dgbg',views.dgbg,name="dgbg"),
    path('home2',views.home2,name="home2"),
    path('srap',views.srap,name="srap"),
    path('dgap',views.dgap,name="dgap"),
    path('drs',views.drs,name="drs"),
    path('hospital',views.hospital,name="hospital"),
    path('bloodstock',views.bloodstock,name="bloodstock"),
    path('us',views.us,name="us"),
    path('bus',views.bus,name="bus"),
    path('bloodgroup',views.bloodgroup,name="bloodgroup"),
    path('login1',views.login1,name="login1"),

]
