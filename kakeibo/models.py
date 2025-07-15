"""

    家計簿アプリ
    データモデル

    File name : models.py
    Date : 2025.06.04
    Written by : Hamada Jo

"""
from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    """
        カテゴリーのテーブル

        支出の種類を選び、項目を追加または削除することができる

        name : カテゴリの名前
    """
    #フィールドの定義
    name=models.TextField()

    def __str__(self):
        del self.name #カテゴリーを消す
        return self.name #カテゴリー名を表示させる



class Manage(models.Model):
    """
        家計簿作成クラス

        date : 日付
        category:カテゴリ(買った種類)
        cost : 金額
        memo : メモ(カテゴリーを具体的に)
    """
    #フィールドの定義
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #categoryのクラスで登録したcategoryをここで表示させ、選択式にする
    cost = models.IntegerField() #数字のみ打ち込む
    memo = models.TextField()

    def __str__(self):
        return self.date,self.category #カテゴリー名を表示させる
