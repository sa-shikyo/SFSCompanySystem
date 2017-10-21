# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-08 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, verbose_name='社員コード')),
                ('name', models.CharField(max_length=100, verbose_name='社員名')),
                ('phonetic', models.CharField(max_length=100, verbose_name='フリガナ')),
                ('sex', models.CharField(max_length=2, verbose_name='性別')),
                ('email', models.EmailField(max_length=255, verbose_name='メールアドレス')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='入社日')),
                ('post', models.CharField(max_length=10, verbose_name='〒')),
                ('adress', models.CharField(max_length=100, verbose_name='住所')),
            ],
            options={
                'verbose_name': '社員情報',
                'verbose_name_plural': '業務 : 社員情報 (m_members)',
                'db_table': 'm_members',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='メールアドレス')),
                ('user_name', models.CharField(max_length=100, verbose_name='ユーザー名')),
                ('password', models.CharField(max_length=100, verbose_name='パスワード')),
                ('apply_begin', models.DateField(default=django.utils.timezone.now, verbose_name='適用開始日')),
                ('apply_end', models.DateField(default='9999-12-31', verbose_name='適用開始日')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
            options={
                'verbose_name': 'アカウント',
                'verbose_name_plural': '業務 : アカウント (m_users)',
                'db_table': 'm_users',
                'ordering': ['-id'],
            },
        ),
    ]
