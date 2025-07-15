"""
    家計簿アプリ
    admin用の設定

    File name:admin.py
    Date:2025.06.04
    Written by:Hamada Jo

"""
from django.contrib import admin
from .models import Manage
from .models import Category

admin.site.register(Manage)
admin.site.register(Category)
