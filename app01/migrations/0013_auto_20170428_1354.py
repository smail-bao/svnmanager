# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_svn_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='online_permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_info', models.CharField(blank=True, max_length=100, null=True)),
                ('web_users', models.CharField(max_length=100)),
                ('src_dir', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '\u4e0a\u7ebf\u4ee3\u7801\u6743\u9650\u8868',
                'verbose_name_plural': '\u4e0a\u7ebf\u4ee3\u7801\u6743\u9650\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('views_svns_list', '\u67e5\u770bsvn\u7248\u672c\u5e93\u4fe1\u606f\u8868'), ('views_onlinecode_info', '\u67e5\u770b\u63a8\u9001\u4ee3\u7801\u8be6\u7ec6\u4fe1\u606f\u8868'), ('views_assets_info', '\u67e5\u770b\u8d44\u4ea7\u8be6\u7ec6\u4fe1\u606f\u8868')), 'verbose_name': '\u9875\u9762\u6743\u9650\u8868', 'verbose_name_plural': '\u9875\u9762\u6743\u9650\u8868'},
        ),
    ]
