# -*- coding: utf-8 -*-

from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_http_methods(["GET", "POST"])
def cms_login(request):
	return render(request, 'cms/cms_login.html', {})

@require_http_methods(["GET", "POST"])
def cms_menu(request):
	aaa = "123456"
	return render(request, 'cms/menu.html', {'aaa': aaa})