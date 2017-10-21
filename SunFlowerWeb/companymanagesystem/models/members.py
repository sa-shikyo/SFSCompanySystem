# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Members(models.Model):
    """
    社員情報テーブル(m_members)
    """

    code        = models.CharField(_(u'社員コード'), max_length=5, null=False, blank=False)
    name        = models.CharField(_(u'社員名'), max_length=100, null=False, blank=False)
    phonetic    = models.CharField(_(u'フリガナ'), max_length=100, null=False, blank=False)
    sex         = models.CharField(_(u'性別'), max_length=2, null=False, blank=False)
    email       = models.EmailField(_(u'メールアドレス'), max_length=255, null=False, blank=False)
    create_date = models.DateField(_(u'入社日'), null=False, blank=False, default=timezone.now)
    post        = models.CharField(_(u'〒'), max_length=10, null=False, blank=False)
    adress      = models.CharField(_(u'住所'), max_length=100, null=False, blank=False)

    class Meta:
        app_label = 'companymanagesystem'
        db_table  = 'm_members'
        verbose_name = _(u'社員情報')
        verbose_name_plural = _(u'業務 : 社員情報 (%s)' % db_table)
        ordering = ['-id', ]
