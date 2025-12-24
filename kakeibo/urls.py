"""
    Blogアプリ
    URL定義

    Filename urls.py
    Date:2025.4.2
    written by:Hamada Jo

"""
from django.urls import path
from . import views

app_name='kakeibo' #アプリケーション名
urlpatterns=[
    path('',views.manage_list,name='kakeibo_list'),
]
