# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from companymanagesystem.models import Users
from companymanagesystem.models import Members


admin.site.unregister(Group)
admin.site.unregister(User)

# admin.site.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'user_name', 'apply_begin', 'apply_end', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(Users, UsersAdmin)

# admin.site.register()
class MembersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code', 'name', 'phonetic', 'sex', 'email', 'create_date', 'post', 'adress',
    )
    ordering = ('-id',)
    pass
admin.site.register(Members, MembersAdmin)

admin.site.register(Session)