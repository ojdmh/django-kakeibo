"""
    Accountsアプリ
    URL定義

    Filename urls.py
    Date: 2026.02.04
    Written By Hamada Jo

"""
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('profile/update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]
