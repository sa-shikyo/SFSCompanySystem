# -*- coding: utf-8 -*-

from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from companymanagesystem.models import Members

@require_http_methods(["GET", "POST"])
def cms_login(request):
    return render(request, 'cms/cms_login.html', {})

@require_http_methods(["GET", "POST"])
def cms_menu(request):
    return render(request, 'cms/menu.html', {})

@require_http_methods(["GET", "POST"])
def cms_member_info(request):
    """
    社員情報
    """

    # --------------
    # 社員情報の取得
    # --------------
    member_list = Members.objects.filter().order_by('id')
    return render(request, 'cms/member_list.html', {
        'member_list': member_list,
    })