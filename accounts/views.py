"""
    Accounts 表示部分

    Filename views.py
    Date: 2026.02.04
    Written By Hamada Jo

"""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from django.shortcuts import resolve_url
from .forms import UserUpdateForm
from django.contrib.auth.models import User

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        """
                ユーザが一致する場合とスーパーユーザの場合許可する
        """
        user=self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin,DetailView):
    """
            ユーザの詳細を表示するビュー
    """
    model=User
    template_name="accounts/user_detail.html"


class UserUpdate(OnlyYouMixin,UpdateView):
    """
            ユーザ情報を更新するビュー
    """
    model=User
    form_class=UserUpdateForm
    template_name="accounts/user_form.html"

    def get_success_url(self):
        """
            更新後の表示をする画面。ユーザの詳細を表示する画面に遷移する。
        """
        return resolve_url("accounts:user_detail",pk=self.kwargs['pk'])
