"""
    kakeiboアプリ
    家計簿サイトの表示

    Filename views.py
    Date:2025.4.2
    written by:Jo hamada

"""
from django.shortcuts import render
from django.views.generic import View, DetailView
from django.utils import timezone
from .models import Manage


class ManageListView(View):
    def get(self,request,*args,**kwargs):
        """
            Get request用の処理
            ブログ記事一覧を表示する
        """
        context={}
        #記事データを取得
        posts=Manage.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        context['posts']=posts
        return render(request,"blog/_list.html",context)

post_list=ManageListView.as_view()

class ManageDetailView(DetailView):
    model=Manage
    template_name="blog/post_detail.html"

post_detail=ManageDetailView.as_view()
