"""
    kakeiboアプリ
    家計簿サイトの表示(管理画面ではない)

    Filename views.py
    Date:2025.4.2
    written by:Jo hamada

"""
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import Manage

class ManageListView(View):
    def get(self,request,*args,**lwargs):
        """
            Get request用の処理
            家計簿の一覧を表示する
        """
        context={}
        #家計簿のManageのデータを取得
        lists=Manage.objects.filter(date=timezone.now()).order_by("-date")
        context['lists']=lists
        Manage.number+=1

        return render(request,"kakeibo/kakeibo_list.html",context)

manage_list=ManageListView.as_view()
